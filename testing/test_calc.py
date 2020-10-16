#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest

from pythoncode.calculator import Calculator

class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("\n计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 2, 3], [100, 200, 300], [0.1, 0.1, 0.2], [-1, -2, -3], [1, 0, 1]
    ], ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[
        [1,2,2],[300,400,120000],[0.1,0.9,0.09],[-1,-3,3],[4,0,0]
        ],ids=['int_case','bignum_case','float_case','minus_case','zero_case'])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[
        [4,2,2],[1000,200,5],[0.9,0.3,3],[-9,-3,3],[9,0,'除数不能为0'],[0,9,0]],
        ids=['int_case','bignum_case','float_case','minus_case','zero_1_case','zero_1_case'])
    def test_div(self,a,b,expect):
        result = self.calc.div(a,b)
        # print(expect)
        assert result == expect