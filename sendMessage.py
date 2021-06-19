import json
import requests

"""
    @ Author    : hong-il
    @ Date      : 2021-06-19
    @ File name : sendMessage.py
    @ File path : 
    @ Description : App Home 에서 App 이름 설정
"""


class SendMessage:

    def __init__(self, token_info):
        self.token = token_info

    def run(self):
        self.post_message('#금융-솔루션', 'Hello World!')

    def post_message(self, channel, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
                                 headers={"Authorization": "Bearer " + self.token},
                                 data={"channel": channel, "text": text}
                                 )


def main():
    with open("config.json") as config_file:
        config = json.load(config_file)
        token_info = config.get("token")

    sendMessage = SendMessage(token_info=token_info)
    sendMessage.run()


if __name__ == '__main__':
    main()
