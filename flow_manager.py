import json
from dialogflow_v1 import DialogflowApi

token_list = {
              'main_page': 'f06ad886f01f4053b13e58116580a090',
              'list_page': '0695ab771d6442b6b94281981042838b',
              'detail_page':'a75f9e59d9b7482d8ba89ef198e509ad',
              'confirm_page': '0e4800ee137944d7a196997baae98102'
              }

action_format = {
                'current_page':None,
                'destination_page':None,
                'Speech':None,
                'Entity': None
                }

intent_name = None
action_complete = None

def flow_control(dataJson):
    dataStr = json.loads(dataJson)
    a = DialogflowApi(client_token = token_list[dataStr['currentPage']])
    df_response = a.post_query(dataStr['query'])
    response = df_response.json()
    print(response)

    if 'intentName' in response['result']['metadata']:
        intent_name =  response['result']['metadata']['intentName'] 
    else:
        intent_name = None

    print(intent_name)
    action_format['current_page'] = dataStr['currentPage']
    action_format['Speech'] = response['result']['fulfillment']['speech']

    if 'parameters' in response['result']:
        action_format['Entity'] = response['result']['parameters']
    else:
        action_format['Entity'] = None

    return json.dumps(action_format)

def destination_handler(current_page, intent_name):
    
    return response
