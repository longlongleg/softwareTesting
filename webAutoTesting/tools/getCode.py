#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 14:43
# @Author : lumi
# @File : getCode.py
# @Software: PyCharm

from autoStruct.jingcaiAuto.tools import getTime
from autoStruct.jingcaiAuto.tools import getFileDirectory
import time
from PIL import Image
import base64
import requests

def get_code(driver,xpath):

    t = getTime.get_time()

    path=getFileDirectory.get_directory(getFileDirectory.get_directory())+"\\screenshoot"
    whole_picture_name=path+"\\"+str(t)+".png"

    time.sleep(1)
    #截取整个页面的图进行保存

    driver.save_screenshot(whole_picture_name)
    ele = driver.find_element_by_xpath(xpath)

    #rect返回的可以构建矩形，xy,表示左上角第一个点的位置，height，width表示宽跟高度
    ele_svg = ele.rect
    #print(ele_svg)
    left_x=ele_svg['x']
    left_y=ele_svg['y']
    right_x=left_x+ele_svg['width']
    right_y=left_y+ele_svg['height']

    #在上面截取的整个页面上面截取验证码部分进行保存为图片
    img = Image.open(whole_picture_name)
    code_picture=img.crop((left_x,left_y,right_x,right_y))
    part_picture_name=path+"\\"+str(getTime.get_time())+".png"
    code_picture.save(part_picture_name)
    #print(part_picture_name)

    #获取验证码图片的内容,使用python自带的,识别不是很精准，要求图片分片率高 清晰
    '''code1 = pytesseract.image_to_string(part_picture_name)
    print(code1)'''

    #第三方库精准使用 百度通用文字识别,识别精准
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
    # 二进制方式打开图片文件
    f = open(part_picture_name, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = '24.c2b7e4a140df5f36c0e375b631ff0502.2592000.1626937854.282335-24417167'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)


    if response.json()['words_result'] == []:

        return '666'

    else:
        #print(response.json())
        code = response.json()['words_result'][0]['words']
        #print(code)
        return code.strip()

