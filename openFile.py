import json

"""
    @ Author    : hong-il
    @ Date      : 2021-06-19
    @ File name : openFile.py
    @ File path : 
    @ Description : 
"""


class Config:

    def __init__(self, token_info):
        self.token = token_info

    def run(self):
        print(self.token)


def main():
    with open("config.json") as config_file:
        config = json.load(config_file)
        token_info = config.get("token")

    config = Config(token_info=token_info)
    config.run()


if __name__ == '__main__':
    main()
