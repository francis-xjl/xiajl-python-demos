#!/usr/bin/env python
# encoding: utf-8
"""
@author: francis
@contact: francis.xjl@qq.com
@file: data_convert_demo
@time: 2018/5/21 21:56
@desc:
"""
import pandas

def list_to_dataframe():
    list = [[1,'aa',3],[2,'cc', 4],[4, 'dd', 1],[4, 'ee', -1]]
    # list = [(1, 'aa', 3), (2, 'cc', 4), (4, 'dd', 1), (4, 'ee', -1)]
    indexs = [x for x, y, z in list]
    pd = pandas.DataFrame(list, index=indexs,columns=["first", "second", "third"])
    print(pd)

if __name__ == "__main__":
    list_to_dataframe()