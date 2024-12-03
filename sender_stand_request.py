import requests
import configuration
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.POST_CREATE_USER_PATH,
                         headers=data.user_headers,
                         json=user_body)

def get_new_user_token():
    return post_new_user(data.user_body).json()["authToken"]

def get_kit_headers():
    current_headers = data.kit_headers.copy()
    current_headers["Authorization"] = 'Bearer ' + get_new_user_token()
    return current_headers

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.POST_CREATE_KIT_PATH,
                         headers=get_kit_headers(),
                         json=kit_body)