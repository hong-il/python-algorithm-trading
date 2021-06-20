"""
    @ Author    : hong-il
    @ Date      : 2021-06-19
    @ File name : sendMessage.py
    @ File path : 
    @ Description : App Home 에서 App 이름 설정
"""
import json
import requests


class SendMessage:

    @staticmethod
    def post_message(channel, text):
        with open("config.json") as config_file:
            config = json.load(config_file)
            token_info = config.get("token")
        response = requests.post("https://slack.com/api/chat.postMessage",
                                 headers={"Authorization": "Bearer " + token_info},
                                 data={"channel": channel, "text": text}
                                 )
