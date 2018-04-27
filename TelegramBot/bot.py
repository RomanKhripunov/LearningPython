import json
import os.path
import requests
import time

from fine_getter import get_fines


# https://api.telegram.org/bot280063928:AAHt3BF2BV1SyW_a547eZZ3PakkExdWsHzI/getMe
token = "280063928:AAHt3BF2BV1SyW_a547eZZ3PakkExdWsHzI"
TELEGRAM_BOT_URL = "https://api.telegram.org/bot" + token + "/"
LAST_UPDATE_ID = 0


def write_response_to_file(json_data, rewrite_file=False):
    """This method write response.json data to file if need to debug info"""
    file_name = "updates.json"
    if rewrite_file:
        with open(file_name, "w") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)


def get_updates():
    """Method takes all available message which client sent"""
    url = TELEGRAM_BOT_URL + "getUpdates"
    response = requests.get(url)
    json_response = response.json()
    write_response_to_file(json_response, rewrite_file=False)
    return json_response


def get_message():
    """Method takes a last message from all messages"""
    last_object = get_updates()["result"][-1]
    current_update_id = last_object["update_id"]

    global LAST_UPDATE_ID
    if current_update_id != LAST_UPDATE_ID:
        LAST_UPDATE_ID = current_update_id
        chat_id = last_object["message"]["chat"]["id"]
        text_message = last_object["message"]["text"]

        message_info = {
            "chat_id": chat_id,
            "text": text_message
        }
        return message_info
    return None


def send_message(chat_id, text="Wait wait wait"):
    """Method send message to client"""
    url = TELEGRAM_BOT_URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)


def main():
    while True:
        answer = get_message()

        if answer is not None:
            chat_id = answer["chat_id"]
            text = answer["text"]

            if text == "/fine":
                send_message(chat_id, get_fines())
        time.sleep(2)


if __name__ == '__main__':
    main()
