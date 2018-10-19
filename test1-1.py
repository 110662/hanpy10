import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1('Hello はんなり Python!',
        style = {
        'textAlign': 'center',
        'color': 'blue'
        }),
    html.P('はんなりPythonは、はんなりとPythonについて話し合うグループです。',
        style = {
        'textAlign': 'center',
        'color': colors['text']
        }),
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': 'white',
                'paper_bgcolor': 'white',
            }
        }
    )])


if __name__ == '__main__':
    app.run_server(debug=True)