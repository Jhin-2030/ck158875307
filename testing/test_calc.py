#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import yaml

from pythoncode.calculator import Calculator

# 解析测试数据的数据驱动
def get_datas():
    with open("D:/AutoTestStudy/HogwartsSDET15/testing/datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    add_float_datas = datas['add_float']['datas']
    add_float_ids = datas['add_float']['ids']
    sub_datas = datas['sub']['datas']
    sub_ids = datas['sub']['ids']
    mul_datas = datas['mul']['datas']
    mul_ids = datas['mul']['ids']
    mul_float_datas = datas['mul_float']['datas']
    mul_float_ids = datas['mul_float']['ids']
    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']
    div_zero_datas = datas['div_zero']['datas']
    div_zero_ids = datas['div_zero']['ids']
    return [add_datas,add_ids,add_float_datas,add_float_ids,sub_datas,sub_ids,mul_datas,mul_ids,mul_float_datas,mul_float_ids,div_datas,div_ids,div_zero_datas,div_zero_ids]
    # return [div_zero_datas,div_zero_ids]

# 解析测试步骤的数据驱动
# def get_steps(addstepsfile,calc,a,b,expect):
#     with open("./steps/add_steps.yml") as f:
#         steps = yaml.safe_load(f)
#     for step in steps:
#         if 'add' == step:
#             result = calc.add(a,b)
#         elif 'add1' == step:
#             result = calc.add1(a,b)
#         assert result == expect

class TestCalc:
    # def setup_class(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("\n计算结束")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect',get_datas()[0],ids=get_datas()[1])
    def test_add(self,count,a,b,expect):
        result = count.add(a,b)
        assert result == expect

    # 浮点数相加位数有误的处理
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect',get_datas()[2],ids=get_datas()[3])
    def test_add_float(self,count,a,b,expect):
        result = count.add(a,b)
        assert round(result,2) == expect

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a,b,expect',get_datas()[4],ids=get_datas()[5])
    def test_sub(self,count,a,b,expect):
        result = count.sub(a,b)
        assert result == expect

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('a,b,expect',get_datas()[6],ids=get_datas()[7])
    def test_mul(self,count,a,b,expect):
        result = count.mul(a,b)
        assert result == expect

    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('a,b,expect',get_datas()[8],ids=get_datas()[9])
    def test_mul_float(self,count,a,b,expect):
        result = count.mul(a,b)
        assert round(result,2) == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect',get_datas()[10],ids=get_datas()[11])
    def test_div(self,count,a,b,expect):
        result = count.div(a,b)
        assert result == expect

    # 异常情况，除数为 0 的用例
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b',get_datas()[12],ids=get_datas()[13])
    def test_div_zero(self,count,a,b):
        with pytest.raises(ZeroDivisionError):
            count.div(a, b)
