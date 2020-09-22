from flask import jsonify, request
import dash
import time
import multiprocessing
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq

app = dash.Dash(__name__, url_base_pathname='/app/',
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
"""
timer = dcc.Interval(
    id='interval-component',
    interval=1*2000,  # in milliseconds
    n_intervals=0,
    disabled=True,
)
"""
Navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="http://www.cea.fr")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],

    brand="SINBAD",
    brand_href="#",
    sticky="top",
)

index_page = html.Div([
    Navbar,
    html.Div('show this content'),
    dbc.NavItem(dbc.NavLink("Link", href="http://www.cea.fr")),
    dcc.Link('Go to "/result"', href='/result'),
    html.Br(),
    
    dbc.Button("Open collapse",
               id="collapse-button", className="my-2"),

    # timer,
    # body
])


def serve_layout():
    # if flask.has_request_context():
    #     return html.H4("rien encore...")
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(index_page, id='page-content')
    ])


app.layout = serve_layout

#app.layout = html.Div('show this content')


@server.route('/m2')
def route1():
    print("request", request.args.to_dict())
    return jsonify({'message': 'this is the first route!', "lk": [58., 56.],
                    "num proc": multiprocessing.cpu_count(),
                    "time": time.asctime()})


@server.route('/m1/')
def route2():
    print("request m1", request.args.to_dict())
    return jsonify({'message': 'm1', "lk": ["m1", 56.],
                    "num proc": multiprocessing.cpu_count(),
                    "time": time.asctime()})


if __name__ == '__main__':
    server.run(debug=True, port=8050)
