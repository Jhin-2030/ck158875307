#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        self.driver.implicitly_wait(3)      # 隐式等待

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="归入各种类别的所有主题"]').clear()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable)
        # def wait(x):
        #     return  len(self.driver.find_element(By.XPATH,'//*[@class="table-heading"]')) >= 1
        # WebDriverWait(self.driver,10).until(wait)       # 显式等待
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
