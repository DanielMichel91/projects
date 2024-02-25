import requests
import boto3
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
from botocore.errorfactory import ClientError

# Set timezone and get current time and date
german_tz = pytz.timezone("Europe/Berlin")
time_in_ger = datetime.now(german_tz)
current_time = time_in_ger.strftime("%H:%M:%S")
current_date = time_in_ger.strftime("%d.%m.%Y")

# Get Bitcoin price from Coindesk API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
bitcoin_price = data["bpi"]["USD"]["rate"]

# S3 Bucket information
bucket_name = "bitcoin-trader-24-02-2024"
file_name = "bitcoin_prices.csv"
object_name = "trading/" + file_name

# S3 client initialization
s3 = boto3.client("s3")

try:
    # Download existing file from S3
    s3.download_file(bucket_name, object_name, file_name)
except ClientError as e:
    if e.response["ResponseMetadata"]["HTTPStatusCode"] == 404:
        print("Object does not exist.")
        print("A new file bitcoin_prices.csv will be created locally.")
    else:
        print("Some other error occurred.")
        print("Please check your S3 Bucket and this Python Code.")
        sys.exit()
finally:
    # Append current data to the file
    with open(file_name, "a") as file:
        file.write(f'{current_date};{current_time};{bitcoin_price}\n')

# Upload the updated file back to S3
s3.upload_file(file_name, bucket_name, object_name)

# Read the prices from the file into a DataFrame
prices = pd.read_csv(file_name, sep=";", header=None, thousands=",")
prices.columns = ["date", "time", "price"]

# Filter prices for the current date
prices = prices[prices.date == current_date]
prices["price"] = pd.to_numeric(prices["price"])
prices["time"] = pd.to_datetime(prices["time"], format='%H:%M:%S').dt.strftime('%H:%M:%S')

# Plotting and saving the plot
plot_file_name = f'bitcoin_price_{current_date.replace("/","_")}.png'
sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})
sns_plot = sns.lineplot(x="time", y="price", data=prices)
sns_plot.set_title(f'Bitcoin Preise vom {current_date}')
sns_plot.set_ylabel("Bitcoin Preis in $")
sns_plot.set_xticklabels(prices["time"], rotation=45, horizontalalignment='right')
sns_plot.get_figure().savefig(plot_file_name, bbox_inches='tight')
sns_plot.figure.clf()

# Upload the plot to S3
s3.upload_file(plot_file_name, bucket_name, "trading/plots/"+plot_file_name)