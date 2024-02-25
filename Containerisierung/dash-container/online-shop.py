from dynamodb import *
import dash_bootstrap_components as dbc
import dash
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import flask



# app = dash.Dash(__name__)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

fig = px.area(plant_df, x="orderID", y="quantity", color_discrete_sequence=["#ff008b"], labels={"orderID": "Bestelldatum", "quantity": "Bestellmenge"})
fig.update_xaxes(showline=True, linewidth=1, linecolor='black', ticks="outside", tickwidth=2, tickcolor='black', ticklen=5)
fig.update_yaxes(showline=True, linewidth=1, linecolor='black', ticks="outside", tickwidth=2, tickcolor='black', ticklen=5)
fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'
})

book_card = dbc.Card([
    dbc.CardHeader("Book"),
    dbc.CardBody([
        html.Img(src=app.get_asset_url('book.png'), style={'height':'100%', 'width':'100%'}),
        ],
        style={'textAlign': 'center'}
        ),
    dbc.CardFooter(
        html.Div([
            # html.P(get_total_orders('book')),
            html.P(id='update_books'),
            dcc.Interval(id='interval-component-books', interval=10 * 1000, n_intervals=0)]))
            ])
            
shoes_card = dbc.Card([
    dbc.CardHeader("Shoes"),
    dbc.CardBody([
        html.Img(src=app.get_asset_url('sneakers.png'), style={'height':'100%', 'width':'100%'}),
        ],
        style={'textAlign': 'center'}
        ),
    dbc.CardFooter(
        html.Div([
            # html.P(get_total_orders('shoes'))]))
            html.P(id='update_shoes'),
            dcc.Interval(id='interval-component-shoes', interval=10 * 1000, n_intervals=0)]))
            ])
            
plant_card = dbc.Card([
    dbc.CardHeader("Plant"),
    dbc.CardBody([
        html.Img(src=app.get_asset_url('spider-plant.png'), style={'height':'100%', 'width':'100%'}),
        ],
        style={'textAlign': 'center'}
        ),
    dbc.CardFooter(
        html.Div([
            # html.P(get_total_orders('plant'))]))
            html.P(id='update_plant'),
            dcc.Interval(id='interval-component-plant', interval=10 * 1000, n_intervals=0)]))
            ])
    

app.layout = dbc.Container([
    
    html.Div(id="status"),
    
    html.H1("Neue Bestellung anlegen"),
    
    html.Div([html.H6("Bestellinformationen im Format <customerID>,<firstname>,<lastname>,<country>,<product>,<quantity>")]),
    
    html.Div([dbc.Input(id='input-on-submit', type='text')]),
    
    dbc.Button('Submit', id='submit-val', color="primary", n_clicks=0),
    
    html.Div([html.P("Bitte Bestellinformationen eingeben.")]),
    
    html.Div(id='my-output'),
    
    html.Div([html.H1(children="Verkäufe für das Produkt plant")]),
    
    html.Div(children=[html.Div([dcc.Graph(id='graph1',figure=fig)])]),
    
    html.Div([html.H1("Übersicht Produktbestellungen weltweit")]),
    
    dbc.Row([
        dbc.Col(book_card),
        dbc.Col(shoes_card),
        dbc.Col(plant_card)]),
    ])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State('input-on-submit', 'value')
)

def new_order(n_clicks, value):
    if value is not None:
        split_value = value.split(", ")
        if len(split_value) == 6:
            response = table.put_item(Item={
                'customerID': split_value[0],
                'orderID': current_date,
                'firstname': split_value[1],
                'lastname': split_value[2],
                'country': split_value[3],
                'product': split_value[4],
                'quantity': int(split_value[5])})
        else:
            return f'"The input was not correct, please type your <customerID>,<firstname>,<lastname>,<country>,<product>,<quantity>"'
            
            
@app.callback(
    Output(component_id='update_books', component_property='children'),
    Input(component_id='interval-component-books', component_property='n_intervals')
)

def update_books(n):
    return get_total_orders('book')
    
@app.callback(
    Output(component_id='update_shoes', component_property='children'),
    Input(component_id='interval-component-shoes', component_property='n_intervals')
)

def update_shoes(n):
    return get_total_orders('shoes')
    
@app.callback(
    Output(component_id='update_plant', component_property='children'),
    Input(component_id='interval-component-plant', component_property='n_intervals')
)

def update_plant(n):
    return get_total_orders('plant')



if __name__ == '__main__':
    app.run_server(debug=True)
    
# example@muster.com, Max, Muster, Germany, shoes, 16