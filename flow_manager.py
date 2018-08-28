import json
from dialogflow_v1 import DialogflowApi

token_list = {
              'main_page': 'f06ad886f01f4053b13e58116580a090',
              'list_page': '0695ab771d6442b6b94281981042838b',
              'detail_page':'a75f9e59d9b7482d8ba89ef198e509ad',
              'confirm_page': '0e4800ee137944d7a196997baae98102'
              }

page_tuple = ('main_page', 'list_page', 'detail_page', 'confirm_page', None)
action_format = {
                'current_page':None,
                'destination_page':None,
                'Speech':None,
                'Entity': None
                }

intent_name = None
action_incomplete = None

def flow_control(dataJson):
    dataStr = json.loads(dataJson)
    a = DialogflowApi(client_token = token_list[dataStr['currentPage']])
    df_response = a.post_query(dataStr['query'])
    response = df_response.json()
    #print(response)

    if 'intentName' in response['result']['metadata']:
        intent_name =  response['result']['metadata']['intentName'] 
    else:
        intent_name = None

    action_incomplete = response['result']['actionIncomplete']
    action_format['current_page'] = dataStr['currentPage']
    action_format['Speech'] = response['result']['fulfillment']['speech']

    if 'parameters' in response['result']:
        action_format['Entity'] = response['result']['parameters']
    else:
        action_format['Entity'] = None
    
    if dataStr['currentPage'] == 'main_page':
        main_page_handler(dataStr['currentPage'], intent_name, action_incomplete)
    elif dataStr['currentPage'] == 'list_page':
        list_page_handler(dataStr['currentPage'], intent_name, action_incomplete)
    elif dataStr['currentPage'] == 'detail_page':
        detail_page_handler(dataStr['currentPage'], intent_name, action_incomplete)
    else:
        confirm_page_handler(dataStr['currentPage'], intent_name, action_incomplete)

    return json.dumps(action_format)

def main_page_handler(currentPage, intentName, actionIncomplete):
    
    if intentName == 'restaurant_book' and actionIncomplete == False :
        indexOfCurrentPage = page_tuple.index(action_format['current_page'])
        action_format['destination_page'] = page_tuple[indexOfCurrentPage + 1] 
    elif intentName == 'near_me_now' and actionIncomplete == False:    
        indexOfCurrentPage = page_tuple.index(action_format['current_page'])
        action_format['destination_page'] = page_tuple[indexOfCurrentPage + 1] 
    elif intentName == 'browse_by_cuisine' and actionIncomplete == False:
        indexOfCurrentPage = page_tuple.index(action_format['current_page'])
        action_format['destination_page'] = page_tuple[indexOfCurrentPage + 1] 
    elif intentName == 'dinner_tonight' and actionIncomplete == False:
        indexOfCurrentPage = page_tuple.index(action_format['current_page'])
        action_format['destination_page'] = page_tuple[indexOfCurrentPage + 1] 
    else:
        action_format['destination_page'] = action_format['current_page']
    return

def list_page_handler(currentPage, intentName, actionIncomplete):
    action_format['destination_page'] = action_format['current_page']
    return

def detail_page_handler(currentPage, intentName, actionIncomplete):
    action_format['destination_page'] = action_format['current_page']
    return

def confirm_page_handler(currentPage, intentName, actionIncomplete):
    action_format['destination_page'] = action_format['current_page']
    return
