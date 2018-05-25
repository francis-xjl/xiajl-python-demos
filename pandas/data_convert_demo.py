#!/usr/bin/env python
# encoding: utf-8
"""
@author: francis
@contact: francis.xjl@qq.com
@file: data_convert_demo
@time: 2018/5/21 21:56
@desc:
"""
import MySQLdb
import os
import pandas


def list_to_dataframe():
    """
    将list 转化为dataframe的示例
    :return:
    """
    list = [[1,'aa',3],[2,'cc', 4],[4, 'dd', 1],[4, 'ee', -1]]
    # list = [(1, 'aa', 3), (2, 'cc', 4), (4, 'dd', 1), (4, 'ee', -1)]
    indexs = [x for x, y, z in list]
    pd = pandas.DataFrame(list, index=indexs,columns=["first", "second", "third"])
    print(pd)


def read_from_mysql():
    """
    将mysql表里的数据转化为pandas对象
    :return:
    """
    mysql_con = MySQLdb.connect(host='127.0.0.1', port=3306, user='roomt', passwd='123456', db='easywork', charset="utf8")
    data = pandas.read_sql('select id,name from room;', con=mysql_con, index_col="id")
    mysql_con.close()
    print data


def read_from_excel():
    """
    将excel里的数据转化为pandas对象
    :return:
    """
    current_folder = os.path.split(os.path.realpath(__file__))[0]
    data = pandas.read_excel(current_folder + "/view_info.xlsx", index_col="vi_id")
    return data



if __name__ == "__main__":
    list_to_dataframe()
    # read_from_mysql()
    read_from_excel()