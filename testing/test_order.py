#!/usr/bin/env python
#-*- utf-8 -*-

import pytest

class TestPytest(object):

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("test_two,测试用例")

    @pytest.mark.run(order=3)
    def test_one(self):
        print("test_one,测试用例")

    @pytest.mark.run(order=1)
    def test_three(self):
        print("test_three,测试用例")