#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/8/4 15:12
# @Author : lumi
# @File : testapi.py
# @Software: PyCharm
import json

import pytest

from autoStruct.apiAuto.common.requests import Request
from autoStruct.apiAutoTesting.common.readConfig import ReadConfig
from autoStruct.apiAutoTesting.excel.readExcel import ReadExcel


class TestApi:

    def setup_class(self):
        file_path = ReadConfig().get_data('excel', 'file_path')
        sheet_name = ReadConfig().get_data('excel', 'sheet_name')
        self.ex = ReadExcel(file_path, sheet_name)

    @pytest.mark.parametrize('num',[1,2,3,4,5])
    def testcase(self,num):
            data = self.ex.get_data(num)
            print(data)
            if data[3]==None:
                r = Request().choose_method(data[1],data[0],data[4],json.loads(data[2]),data[3])
            else:
                r = Request().choose_method(data[1], data[0], data[4], json.loads(data[2]), json.loads(data[3]))
            print(r.text)


if __name__ == '__main__':
    pytest.main(['-vs','testapi.py'])

