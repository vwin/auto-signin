# -*- coding: utf-8 -*-
# Created by Duanwei on 2018/8/21

"""
自动签到启动脚本
"""

from urllib import request
import json


def signin(web_dict, cookie):
    host = web_dict["host"]
    if host:
        print(host)
        url = "http://" + web_dict["host"] + web_dict["url"]
        print(url)
        req = request.Request(url, method="POST")
        headers = web_dict["headers"]
        headers["Cookie"] = cookie
        req.headers = headers
        with request.urlopen(req) as f:
            try:
                res_bytes = f.read()
                print(type(res_bytes))
                print(str(res_bytes, encoding="utf-8"))
            except Exception as e:
                raise e


def signin_all():
    with open("./signin_template.json", "r", encoding="utf-8") as load_f:
        template = json.load(load_f)
        with open("./user_cookies.json", "r", encoding="utf-8") as users_f:
            users = json.load(users_f)
            for user in users:
                web_type = user["type"]
                try:
                    signin(template[web_type], user["cookie"])
                except BaseException as e:
                    print(e)
