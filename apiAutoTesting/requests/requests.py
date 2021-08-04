#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/8/4 14:57
# @Author : lumi
# @File : requests.py
# @Software: PyCharm
import json

import requests


class Request:


    def get_url(self,url,headers=None,paras=None):

        if url==None:
            print("URL地址为空")
        elif paras == None:
            r = requests.get(url,headers=headers,params=paras)
        else:
            r = requests.get(url, headers=headers, params=json.loads(paras))
        return r

    def post_url(self,url,content_type,headers=None,payload=None):

        if url==None:
            print("URL地址为空")
        else:
            if content_type == "application/json":
               payload_json = json.dumps(payload)
               r = requests.post(url,headers=headers,data=payload_json)

            elif content_type =="application/x-www-form-urlencoded":
                r = requests.post(url,headers=headers,data=payload)
            else:
                print("no this content-type")

            return r


    def choose_method(self,method,url,content_type,headers=None,payload=None):
        if method == "get":
            return self.get_url(url,headers,payload)
        elif method == "post":
            return self.post_url(url,content_type,headers,payload)
        else:
            print("no this method request")