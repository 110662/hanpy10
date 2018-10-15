import datetime
import dash 
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id = 'livetext'),
    dcc.Interval(
        id = 'interval_comp',
        #interval = 1000, 
        n_intervals = 0)])

@app.callback(dash.dependencies.Output(component_id = 'livetext', component_property = 'children'),
    [(dash.dependencies.Input(component_id = 'interval_comp', component_property = 'n_intervals'))])
def update(n):
    t = datetime.datetime.now()
    return t

if __name__ == '__main__':
    app.run_server(debug=True)