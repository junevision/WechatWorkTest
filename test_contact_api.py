#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_contact_api.py
@time: 2021/3/26 10:42
@desc: 
"""
import requests


class TestContactAPI:
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwc377ce4b04b0ffd7&corpsecret=ryqrRFdwUe7LZRKeHKgaUjGJ-A6u0KF3B-qMXmzvzqM"
        r = requests.get(url=url)
        token = r.json()['access_token']
        return token

    def test_defect_member(self):
        user_id = "hermione"
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.get_token()}&userid={user_id}'
        r = requests.get(get_member_url)
        print(r.json())
        assert "Hermione" == r.json()['name']

    def test_update_member(self):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.get_token()}'
        data = {
            "userid": "test006",
            "name": "HarryPotter",
            "mobile": "13800099999",
        }
        r = requests.post(url=update_member_url, json=data)
        print(r.json())
        assert "updated" == r.json()['errmsg']

    def test_create_member(self):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token()}'
        data = {
            "userid": "Ron111",
            "name": "RonWeasley",
            "mobile": "+86 13811100111",
            'department': [1]
        }
        r = requests.post(url=create_member_url, json=data)
        print(r.json())
        assert "created" == r.json()['errmsg']

    def test_delete_member(self):
        user_id = "test005"
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid={user_id}'
        r = requests.get(delete_url)
        print(r.json())
        assert "deleted" == r.json()['errmsg']
