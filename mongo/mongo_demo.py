#!/usr/bin/env python
# encoding: utf-8
"""
@author: francis
@contact: francis.xjl@qq.com
@file: mongo_demo.py
@time: 2018/5/26 19:51
@desc:
"""


from pymongo import MongoClient

conn = MongoClient('192.168.16.49', 27017)
db = conn.bandwidth
db.hw_201804_origin.drop()
hw_201804_origin = db.hw_201804_origin
# hw_201804.ensure_index(['room', 'province', 'city', 'dtime'], unique=True)


def buildLine(line):
    info = line.split("\t")
    cbw= {
        "room": info[0],
        "province": info[1],
        "city": info[2],
        "bandwidth": float(info[4].strip())
    }

    return cbw


if __name__ == "__main__":
    i = 0.0
    data = []
    for line in open("/filestep/3576.txt"):
        i = i + 1
        if i % 100000 == 0:
            print "已经读取:%.2f％" % (i / 27443426 * 100)
        if i % 1000000 == 0:
            hw_201804_origin.insert(data)
            data = []
        data.append(buildLine(line))
    hw_201804_origin.insert(data)