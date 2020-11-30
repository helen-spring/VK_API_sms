import os
import requests
import time
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
URL = 'https://api.vk.com/method/users.get'
token = os.getenv('VK_TOKEN')
V = 5.92
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
CLIENT = Client(account_sid, auth_token)
number_from = os.getenv('NUMBER_FROM')
number_to = os.getenv('NUMBER_TO')


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'access_token': token,
        'v': V,
        'fields': 'online'
    }
    response = requests.post(URL, params=params).json()['response']
    return response[0]['online']


def sms_sender(sms_text):
    message = CLIENT.messages.create(
        body=sms_text,
        from_=number_from,
        to=number_to
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
