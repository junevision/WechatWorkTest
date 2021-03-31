#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: wework_contact.py
@time: 2021/3/29 11:54
@desc: 
"""
import requests

from Api.wework.base import Base


class WeworkContact(Base):

    def get_info(self, user_id: str):
        """
        get user information
        :param user_id
        :return:
        """
        get_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid": user_id
        }
        r = self.send("GET", get_member_url, params=params)
        return r.json()

    def create(self, user_id: str, name: str, mobile: str, department: list):
        """
        create member
        :param name
        :param mobile: 手机号 11位
        :param department
        :return:
        """
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            'department': department
        }
        r = self.send("POST", url=create_member_url, json=data)
        return r.json()

    def update(self, user_id: str, name: str):
        """
        update user information
        :param user_id
        :param name
        :return:
        """
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": user_id,
            "name": name
        }
        r = self.send("POST", url=update_member_url, json=data)
        return r.json()

    def delete(self, user_id: str):
        """
        delete member
        :param user_id
        :return:
        """
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            "userid": user_id
        }
        r = self.send("GET", delete_url, params=params)
        return r.json()
