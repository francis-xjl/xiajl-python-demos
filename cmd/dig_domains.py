#!/usr/bin/env python
# encoding: utf-8
"""
@author: francis
@contact: francis.xjl@qq.com
@file: dig_domains
@time: 2018/5/23 14:32
@desc:
"""
import os

domains = ["www.40407.com","www.spdbccc.com.cn","www.wbiao.cn","dujia.jd.com","kj.sscejia.com","pufalicheng.spdbccc.com.cn","fpwyj.spdbccc.com.cn","pfliuliang.spdbccc.com.cn","service.spdbccc.com.cn","www.tuniu.cn","fpsjj.spdbccc.com.cn","www.dfyoo.com","m.wbiao.cn","menpiao.jd.com","kf.40407.com","open.talk-fun.com","insp.spdbccc.com.cn","api.gzrockveda.com","tuniu.com","image.spdbccc.com.cn","ebill.spdbccc.com.cn","static.zhanqi.tv","trace.taiyiplus.com","client2.talk-fun.com","imgssl.suning.com","www.e-nci.com","s.tuniu.com","collect.tuniu.cn","www.sjjinrong.com","search.suning.com","wap.spdbccc.com.cn","respay.suning.com","scs.suning.com","m.tuniu.com","images.taobc.com","passport.suning.com","www.tuniu.com","member.wbiao.cn","cart.wbiao.cn","rpa.tuniu.cn","jr.m.tuniu.com","zhifubao.spdbccc.com.cn","frms-api.tuniu.cn","pgy.tuniu.cn","bjt.dfyoo.com","stgwww.sjjinrong.com","unionpayintl.tuniu.cn","chat.tuniu.com","mct.tuniu.com","img1.haonanren.cm","hotel-openapi.tuniu.cn","secure.tuniu.com","mkk.tuniu.com","www.wbiao.com","gt.tuniu.com","nbd.tuniu.com","khzx.tuniu.com","shark.dfyoo.com","shopping.tuniu.cn","jr.tuniu.com","www.tuniufu.com","api-1.talk-fun.com","nebula.tuniu.cn","payment.tuniu.com","*.tuniu.com","wallet.tuniu.com","memberm.wbiao.cn","qiyehao-ai.tuniu.cn","open-1.talk-fun.com","channels.m.tuniu.com","baoxian.tuniu.com","www.haonanren.cm","mon-api.tuniu.cn","flight-itp.tuniu.cn","jiaotong.tuniu.cn","mall.tuniu.cn","b.tuniu.com","bank-cbhb.tuniu.cn","ttq.spdbccc.com.cn","pay4.gc.com.cn","dc.tuniu.cn","open.tuniu.com","fgs.tuniu.cn","pay.tuniu.com","im.tuniu.com","testwin.taiyiplus.com","i.tuniu.com","weixin.spdbccc.com.cn","m.dfyoo.com","m.tuniu.cn","api.tuniu.cn","tchat.tuniu.com","flight-oai.tuniu.cn","dic.tuniu.com","imcloud.tuniu.com","passport.tuniu.com","frms-new-api.tuniu.cn","tuniufu.com","kai.talk-fun.com","log-1.talk-fun.com","gys.dfyoo.com","bank-ccb.tuniu.cn","bank-njcb.tuniu.cn","open.dfyoo.com","silkroad.tuniu.com","m.wbiao.com","dynamic.m.tuniu.com","bestpay.tuniu.cn","analy.tuniu.cn","8.m.tuniu.com","cashier.tuniu.com","bank-abc.tuniu.cn","wcs-message.tuniu.com","tct-http.tuniu.cn","flight-api.tuniu.com","mbank.spdbccc.com.cn","wechat.tuniu.cn","bjt.tuniu.com","jdb.tuniu.com"]

def dig(domain):
    cmd = "dig %s" % (domain)
    process = os.popen(cmd)
    output = process.read()
    process.close()
    return output

def get_domains_in(domains, keyword, reverse=False):
    """
    根据域名dig的结果来筛选域名。
    如果reverse为False，则表示返回dig结果里包含keyword的域名列表
    如果reverse为True，则表示返回dig结果里不包含keyword的域名列表
    :param domains:
    :param keyword:
    :param reverse:
    :return:
    """
    result = []
    reverse_result = []
    for domain in domains:
        output = dig(domain)
        if keyword in output:
            result.append(domain)
        else:
            reverse_result.append(domain)

    return result if not reverse else reverse_result

if __name__ == "__main__":
    print get_domains_in(domains, "hngsa001", reverse=True)