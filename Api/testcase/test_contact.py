#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_contact.py
@time: 2021/3/29 11:55
@desc: 
"""
import pytest

from Api.wework.wework_contact import WeworkContact


class TestContact:
    name = "Ron_"
    user_id = "Ron001"

    def setup_class(self):
        self.contact = WeworkContact()
        self.mobile = "13800999000"
        self.department = [1]

    def setup(self):
        # handle correct API data
        self.user_id += "tmp"
        self.contact.delete(self.user_id)

    def teardown(self):
        # data clean
        self.contact.delete(self.user_id)

    def test_get_information(self):
        self.contact.create(self.user_id, self.name, self.mobile, self.department)
        # verify user information
        r = self.contact.get_info(self.user_id)
        assert r["name"] == self.name

    def test_create_member(self):
        r = self.contact.create(self.user_id, self.name, self.mobile, self.department)
        assert r.get("errmsg") == "created"
        info = self.contact.get_info(self.user_id)
        assert info["name"] == self.name

    @pytest.mark.parametrize("user_id, new_name", [("tmp", name + "tmp")] * 5)
    def test_update_member(self, user_id, new_name):
        user_id = self.user_id
        self.contact.create(user_id, self.name, self.mobile, self.department)
        r = self.contact.update(user_id, new_name)
        assert r.get("errmsg") == "updated"
        info = self.contact.get_info(user_id)
        assert info["name"] == new_name

    def test_delete_member(self):
        self.contact.create(self.user_id, self.name, self.mobile, self.department)
        r = self.contact.delete(self.user_id)
        assert r.get("errmsg") == "deleted"
        info = self.contact.get_info(self.user_id)
        assert info["errcode"] == 60111
