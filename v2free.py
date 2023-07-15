import json
import logging
import argparse
import os, sys, time, requests

username = sys.argv[1]  # 登录账号
password = sys.argv[2]  # 登录密码


def config_logging():
    logging.basicConfig(filename='flow.log',
                        level=logging.INFO,
                        format="%(asctime)s\t%(levelname)s\t%(message)s")


def v2freeai():
    client = requests.Session()
    login_url = "https://w1.v2free.net/auth/login"
    sign_url = "https://w1.v2free.net/user/checkin"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.net/auth/login",
    }
    data = {
        "email": username,
        "passwd": password,
        "code": "",
    }
    client.post(login_url, data=data, headers=headers)

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.net/user",
    }
    response = client.post(sign_url, headers=headers)

    logging.info("[V2Free]: " + response.json()["msg"])
    print("V2Free" + response.json()["msg"])


if __name__ == "__main__":
    config_logging()
    v2freeai()