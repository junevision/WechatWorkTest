#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: base.py
@time: 2021/3/29 19:15
@desc: 
"""
import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwc377ce4b04b0ffd7",
            "corpsecret": "ryqrRFdwUe7LZRKeHKgaUjGJ-A6u0KF3B-qMXmzvzqM"
        }
        r = self.s.get(url=url, params=params)
        token = r.json()['access_token']
        return token

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
