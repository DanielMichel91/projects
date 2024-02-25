import boto3
client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')
import pandas as pd
from datetime import datetime
import pytz
import matplotlib.pyplot as plt

german_tz = pytz.timezone("Europe/Berlin")
time_in_ger = datetime.now(german_tz)
current_time = time_in_ger.strftime("%H:%M:%S")
current_date = time_in_ger.strftime("%Y%m%d")


response = table.scan()
items = response['Items']
df_table_orders = pd.DataFrame(items)
plant_df = df_table_orders[df_table_orders["product"] == "plant"]
plant_df['orderID'] = pd.to_datetime(plant_df['orderID'], infer_datetime_format=True)

def get_total_orders(productName):
    """Get the sales from the product."""
    response = table.scan()
    items = response['Items']
    df_table_orders = pd.DataFrame(items)
    product_df = df_table_orders[df_table_orders["product"] == productName]
    total_order = product_df['quantity'].sum()
    # total_order = str(total_order)
    return total_order
    # print(total_order)
    # print(type(total_order))
    

if __name__ == '__main__':
    get_total_orders(productName)