from dash import Dash,html,dcc,callback,State,Output,Input
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from components import *
from main import get_reply
@callback(
    Output('main-container', 'className'),
    Input('chat-close-cont', 'n_clicks'),
    State('main-container', 'className')
)
def toggle_chat(n_clicks, current_class):
    if n_clicks is None:
        raise PreventUpdate

    if n_clicks and 'close' in current_class:
        return 'main-container open'
    else:
        return 'main-container close'

@callback(
    Output('chatstore','children',allow_duplicate=True),
    Output('chat','data'),
    Output('query','value'),
    Input('submit-button','n_clicks'),
    Input('query','n_submit'),
    State('query','value'),
    State('chat','data'),
    prevent_initial_call=True
)
def start_chat(n_clicks,m_clicks,query,chat_data):
    if not query:
        raise PreventUpdate
    if n_clicks and not query:
        raise PreventUpdate
    # chat_bubbles =[]
    if chat_data is None:
        chat_data=[]
    # bot_reply = {'sender':'bot','text':'Hi How can i assist you Today'}
    # bot_reply = {'sender':'bot','text':get_reply(query)}
    bot_response = get_reply(query)
    bot_reply = {'sender':'bot','text':bot_response}
    user_reply = {'sender':'user','text':query}
    # chat_bubbles.append(bot_reply)
    # chat_bubbles.append(user_reply)
    chat_data.append(user_reply)
    chat_data.append(bot_reply)
    messages=[]
    for m in chat_data:
        if m['sender']=='user':
            messages.append(usermessage(m['text']))
        else:
            messages.append(botmessage(m['text']))
    clear_value = ""
    
    return html.Div(messages),chat_data,clear_value


@callback(
    Output('main-container','className',allow_duplicate=True),
    Input('close-icon','n_clicks'),
    prevent_initial_call=True
)
def close_chat_icon(n_clicks):
    if not n_clicks:
        return 'main-container open'
    return 'main-container close'
