#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/15 9:26
# @Author : lumi
# @File : test_demo.py
# @Software: PyCharm
from autoStruct.apiAuto.common.common_data import CommData
import pytest

from autoStruct.apiAuto.common.requests import Request


class TestDemo:




    def setup_class(self):
        com = CommData('../excel/request.xlsx', 'Sheet1')
        self.req = Request()
        self.method_list = com.get_methodlist()
        self.url_list = com.get_url_list()
        self.header_list = com.get_header_list()
        self.data_list = com.get_data_list()
        self.content_type_list = com.get_contenttypelist()




    @pytest.mark.parametrize("num",range(0,4))
    def test_api(self,num):

        print(self.method_list[num],self.url_list[num],self.content_type_list[num],self.header_list[num],self.data_list[num])
        r = self.req.choose_method(self.method_list[num],self.url_list[num],self.content_type_list[num],self.header_list[num],self.data_list[num])

        print(r.status_code)
        print(r.text)
        #print(r.content.decode('utf-8')




if __name__ == '__main__':
    pytest.main(['-vs','test_demo.py'])











