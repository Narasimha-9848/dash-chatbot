from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
from components import header,footer
from callbacks import *

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP])


app.layout = dbc.Container([
    html.Div([
    html.Div(
    html.Img(src='/assets/images/chatbot_logo.png', className='bot-logo'),
    id='chat-close-cont',
    n_clicks=0,
    className='chat-close-cont',
),]),
    html.Div([
        html.Div(header()),
        html.Div(id='chatstore',className='chatbox'),
        html.Div([
            html.Div(), html.Div(), html.Div()   # 3 dots
        ], id="loading-spinner", className="spinner", style={"display": "none"}),
        html.Div(style={'margin-top':'10px'}),
        dcc.Store(id='chat'),
        html.Div(footer())
    ],className='main-container close',id='main-container')
])

app.clientside_callback(
    '''
    function(children){
    const chatbox = document.getElementById('chatstore')
    if(chatbox){
    chatbox.scrollTop = chatbox.scrollHeight;
    }
    return children;
    }
    ''',
    Output('chatstore','children',allow_duplicate=True),
    Input('chatstore','children'),
    prevent_initial_call=True
)

app.clientside_callback(
    """
    function(n_clicks, value) {
        const spinner = document.getElementById('loading-spinner');
        if (n_clicks > 0 || value) {
            spinner.style.display = 'flex';   // show spinner
        }
        return window.dash_clientside.no_update;
    }
    """,
    Output('chatstore', 'children',allow_duplicate=True),
    [Input('submit-button', 'n_clicks'),
     Input('query', 'value')],
     prevent_initial_call=True
)

app.clientside_callback(
    """
    function(children) {
        const spinner = document.getElementById('loading-spinner');
        if (spinner) {
            spinner.style.display = 'none';   // hide spinner when response arrives
        }
        return children;
    }
    """,
    Output('chatstore','children'),
    Input('chatstore','children')
)


if __name__ == '__main__':
    app.run(debug=True)