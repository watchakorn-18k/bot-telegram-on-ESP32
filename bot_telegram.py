import urequests
import time
import wifi
import json
import random

wifi.conn_wifi()

BOT_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

offset = None

def send_message(chat_id, text):
    url = BASE_URL + 'sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = urequests.post(url, json=data)
    response.close()

def handle_message(message):
    chat_id = message['chat']['id']
    user_message = message['text']

    phrase = {'Hello': 'Hi!', 'Hi': 'Hello!','ping': 'pong!'}

    random_number = random.randint(0, 10)

    if user_message in phrase:
        send_message(chat_id, phrase[user_message])

    if user_message == 'random':
        send_message(chat_id, random_number)

    if user_message == '/start':
        send_message(chat_id, 'Hi!')
    
def get_updates():
    global offset
    url = BASE_URL + 'getUpdates'
    if offset is not None:
        url += f'?offset={offset}'
    response = urequests.get(url)
    updates = json.loads(response.content)
    response.close()

    for update in updates['result']:
        offset = update['update_id'] + 1
        if 'message' in update:
            handle_message(update['message'])

def main():
    while True:
        get_updates()

if __name__ == '__main__':
    import _thread
    _thread.start_new_thread(main, ())

