from datetime import datetime
import time
import csv
import glob
import numpy as np
import pandas as pd 
import dash 
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    html.Div([
        html.H4('Realtime Sin Graph'),
        html.Div(id='time_now'),
        dcc.Graph(id='sin_now'),
        dcc.Interval(
            id = 'interval-component',
            interval = 1 * 1000,
            n_intervals=0
            )
        ])
    )

@app.callback(Output('time_now', 'children'),
            [Input('interval-component', 'n_intervals')])
def update_title(n):
    t = datetime.now()
    return 'Now is {}!'.format(t)

@app.callback(Output('sin_now', 'figure'),
            [Input('interval-component', 'n_intervals')])
def draw_graph_live(n):
    
    if not glob.glob('data.csv'):
        data = pd.DataFrame()

        t = datetime.now()
        sin_n = np.sin(time.time())

        list_time = []
        list_time.append(t)
        list_sin = []
        list_sin.append(sin_n)

        data['time'] = list_time
        data['sin'] = list_sin

        data.to_csv('data.csv')

        fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b':30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y':1}

        fig.append_trace({
            'x': data['time'],
            'y': data['sin'],
            'name': 'sin',
            'mode': 'lines+markers',
            'type': 'scatter'
            }, 1, 1)

        return fig

    else:
        data = pd.read_csv('data.csv')
        data2 = pd.DataFrame()

        t = datetime.now()
        sin_n = np.sin(time.time())

        list_time = []
        list_time.append(t)
        list_sin = []
        list_sin.append(sin_n)

        data2['time'] = list_time
        data2['sin'] = list_sin

        data = pd.concat([data, data2])

        data.to_csv('data.csv')

 
        fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b':30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y':1}

        fig.append_trace({
            'x': data['time'],
            'y': data['sin'],
            'name': 'sin',
            'mode': 'lines+markers',
            'type': 'scatter'
            }, 1, 1)

        return fig

if __name__ == '__main__':
    app.run_server(debug=True)