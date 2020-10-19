#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pythoncode.calculator import Calculator
import pytest

# @pytest.fixture(scope="module")
# def login():
#     # yield 之前的代码相当于 setup 操作
#     print("登录")
#     #return ('tom','123')
#     # yield 相当于 return 操作
#     yield ['tom','123']
#     # yield 之后的代码相当于 teardown 操作
#     print("注销")
#
# @pytest.fixture(scope="module")
# def operate():
#     print("数据库连接")

@pytest.fixture(scope="module")
def count():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")