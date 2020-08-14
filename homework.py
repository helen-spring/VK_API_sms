import os
import requests
import time
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


def get_status(user_id):
    url = 'https://api.vk.com/method/users.get'
    params = {
        'user_id': user_id,
        'access_token': os.getenv('VK_TOKEN'),
        'v': 5.92,
        'fields': 'online'
    }
    response = requests.post(url, params).json()['response']
    return response[0]['online']


def sms_sender(sms_text):
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_text,
        from_=os.getenv('NUMBER_FROM'),
        to=os.getenv('NUMBER_TO')
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
