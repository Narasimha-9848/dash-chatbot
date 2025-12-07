from dash import Dash,html,dcc
import dash_bootstrap_components as dbc


def header():
    return html.Div([
        html.Div([
            html.Div([
                html.Img(src='/assets/images/chatbot_logo.png',className='bot-logo')
            ]),
             html.Div([
                html.H5('AI CHATBOT',className='chat-heading')
            ]),
            html.Div([
                html.I(className='bi bi-x-square')
            ],className='close-icon',id='close-icon',n_clicks=0)
        ],className='header-cont')
    ])
def footer():
    return html.Div([
      html.Div([
        dbc.Input(type='text',placeholder='Type something here..',id='query',autocomplete='off'),
        dbc.Button(html.I(className='bi bi-send'),n_clicks=0,id='submit-button',className='submit-button')
      ],className='footer-cont')
    ])
def usermessage(text):
    return html.Div([
        html.P(text,className='m-para')
    ],className='user-message')
def botmessage(text):
    return html.Div([
        html.P(text,className='m-para')
    ],className='bot-message')