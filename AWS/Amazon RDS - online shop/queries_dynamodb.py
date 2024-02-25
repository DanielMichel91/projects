import boto3
import pandas as pd
from datetime import datetime
import pytz
import matplotlib.pyplot as plt

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

# Get current time in German timezone
german_tz = pytz.timezone("Europe/Berlin")
time_in_ger = datetime.now(german_tz)
current_time = time_in_ger.strftime("%H:%M:%S")
current_date = time_in_ger.strftime("%Y%m%d")

# Retrieve all items from the table
response = table.scan()
items = response['Items']

# Create a DataFrame from DynamoDB items
df_table_orders = pd.DataFrame(items)

# Filter orders for the "plant" product and sort by orderID
plant_df = df_table_orders[df_table_orders["product"] == "plant"]
plant_df = plant_df.sort_values(by='orderID')

# Convert orderID to datetime format
plant_df['orderID'] = pd.to_datetime(plant_df['orderID'], infer_datetime_format=True)

def get_total_orders(productName):
    """Get the total quantity of orders for a given product."""
    response = table.scan()
    items = response['Items']
    df_table_orders = pd.DataFrame(items)
    
    # Filter orders for the specified product
    product_df = df_table_orders[df_table_orders["product"] == productName]
    
    # Calculate the total quantity of orders
    total_order = product_df['quantity'].sum()
    
    return total_order

# Example usage
if __name__ == '__main__':
    print(get_total_orders("book"))