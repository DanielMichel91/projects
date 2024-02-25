from sqlalchemy import create_engine, text
import MySQLdb
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import boto3
import json

# Create a SQLAlchemy engine
engine = create_engine(f'mysql+mysqldb://admin:pw@database-vscode.cbg0bcqreeou.eu-central-1.rds.amazonaws.com/classicmodels')

# Define SQL queries
querie_order = "SELECT DATE_FORMAT(orderDate, '%%M %%Y') as orderDate, count(orderNumber) as totalOrders from orders GROUP BY YEAR(orderDate), MONTH(orderDate);"
querie_sales = "select customerName, count(*) as total from orders inner join customers using (customerNumber) group by customerNumber order by total desc limit 10;"
querie_customers = "select lastName as employees, count(*) as total from employees left join customers on employeeNumber=salesRepEmployeeNumber group by lastName order by total desc limit 10;"
querie_country = "select country, count(*) as total from customers group by country order by total desc limit 10;"


# Connect to the database and execute queries
with engine.connect() as conn:
    df_order_dict = pd.read_sql(querie_order, conn)
    df_sales_rep = pd.read_sql(querie_sales, conn)
    df_customers = pd.read_sql(querie_customers, conn)
    df_country = pd.read_sql(querie_country, conn)

# Create a Dash web application
app = Dash(__name__)

# Create plots using Plotly Express
fig = px.area(df_order_dict, x="orderDate", y="totalOrders", title="Bestellungen pro Monat", labels={"orderDate": "", "totalOrders": "Anzahl der Bestellungen pro Monat"})
fig2 = px.bar(df_sales_rep, x="total", y="customerName", barmode="group", title="Produktivität", labels={"customerName": "Name des Unternehmens", "total": "Anzahl an Kunden in Betreuung"})
fig3 = px.bar(df_customers, x="employees", y="total", barmode="group", title="Kunden mit den meisten Bestellungen", labels={"employees": "Name des Kunden", "total": "Anzahl an Bestellungen in den Jahren 2003-2005"})
fig4 = px.bar(df_country, x="country", y="total", barmode="group", title="Kundenverteilung weltweit", labels={"country": "Land", "total": "Anzahl an Kunden in der Datenbank"})

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.Div([
        html.H1(children='orders per month'),
        html.Div(children='''
        Dash: First graph.'''),

        dcc.Graph(
            id='graph1',
            figure=fig
        ),
    ]),
    html.Div([
        html.H1(children='sales'),
        html.Div(children='''
        Dash: second graph.'''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),
    ]),
    html.Div([
        html.H1(children='customers'),
        html.Div(children='''
        Dash: third graph.'''),

        dcc.Graph(
            id='graph3',
            figure=fig3
        ),
    ]),
    html.Div([
        html.H1(children='country'),
        html.Div(children='''
        Dash: fourth graph.'''),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),
    ]),
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)