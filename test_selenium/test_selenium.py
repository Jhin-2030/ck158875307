#!/usr/bin/env python
#-*- coding:utf-8 -*-

import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")