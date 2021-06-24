"""
    @ Author    : hikim
    @ Date      : 2021-06-19
    @ File name : sendMessage.py
    @ File path :
    @ Description : Slack 메세지 전송 표준화
"""
import json
import requests


class SendMessage:
    def __init__(self):
        with open("config.json") as config_file:
            token_info = json.load(config_file)
            self.alarm_token = token_info.get("alarm_token")
            self.error_token = token_info.get("error_token")

    def alarm_message(self, channel, attachments):
        data = {
            'channel': channel,
            'attachments': attachments
        }
        requests.post("https://slack.com/api/chat.postMessage",
                      headers={"Authorization": "Bearer " + self.alarm_token, 'Content-Type': 'application/json'},
                      data=json.dumps(data)
                      )

    def error_message(self, channel, attachments):
        data = {
            'channel': channel,
            'attachments': attachments
        }
        requests.post("https://slack.com/api/chat.postMessage",
                      headers={"Authorization": "Bearer " + self.error_token, 'Content-Type': 'application/json'},
                      data=json.dumps(data)
                      )
