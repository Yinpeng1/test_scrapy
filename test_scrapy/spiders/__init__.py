# # This package will contain the spiders of your Scrapy project
# #
# Please refer to the documentation for information on how to create and manage
# your spiders.
from urllib.parse import unquote
import zlib
import gzip
import time
import requests
from urllib import parse
import re
import json
import random
#
# print(unquote('https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18107698208687623114_1559015067800&params=%7B%22type%22%3A0%2C%22objid%22%3A0%2C%22page%22%3A4%2C%22ajax%22%3A1%2C%22retina%22%3A0%7D&_=1559016005577'))
#
# # data = gzip.decompress(b"\u3010\u5e74\u540e\u89e3\u95f7\ud83e\udd32\u3011\u5b81\u9759\u4e0e\u55a7\u56a3\uff0c\u6b65\u5165\u6f33\u5dde\uff0c\u63a2\u7d22\u672a\u77e5\u7684\u571f\u697c\u5473\u9053\u2014")
# # print(data)
# # print(time.time())
#
# # print("\u3010\u5e74\u540e\u89e3\u95f7\u3011")
#
# currentTime = str(time.time() * 1000).split('.')[0]
# params = '{"type":0,"objid":0,"page": '+str(4)+',"ajax":1,"retina":0}'
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
# }
# next_url = 'https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18106270182851686801_1559042985551&params='+ parse.quote(params) + '&_='+currentTime
# print("nextUrl ====>%s" % next_url)
# # encode_url = unquote(next_url)
# # print("encode_url ====>%s" % encode_url)
# next_res = requests.get(next_url, headers=headers)
# # reg = re.compile(r'jQuery18106270182851686801_1559042985551(.*)')
# # reg = re.compile(r'<a href=.*>(.*)<\\\\\/a>')
# html = re.findall(reg, repr(next_res.content))
# print(html)
# for i in html:
#     data = i.encode("utf-8").decode("utf-8")
#     print(data)
#
# # unicode解码
# data = "\u5f18\u5927\u8857\u5934\u8d70\u5341\u904d\uff01\uff01\uff01\u9996\u5c14\u4e94\u5929\u56db\u591c\u5927\u66b4\u8d70\u3010\u8857\u666f\u56fe\u96c6\u3011".encode("utf-8").decode("utf-8")
#
# print("decode: ", data)
# # print("\u5f18\u5927\u8857\u5934\u8d70\u5341\u904d\uff01\uff01\uff01\u9996\u5c14\u4e94\u5929\u56db\u591c\u5927\u66b4\u8d70\u3010\u8857\u666f\u56fe\u96c6\u3011")
# print(parse.unquote("%E7%99%BD%E5%BA%86%E7%8E%B2"))
# proxies = {}
# ip_cache = []
# s = '{"code":0,"success":true,"msg":"0","data":[{"ip":"58.218.200.226","port":2724,"outip":"119.133.130.199"},{"ip":"58.218.200.226","port":7195,"outip":"182.100.144.40"},{"ip":"58.218.200.225","port":4601,"outip":"117.179.160.209"},{"ip":"58.218.200.226","port":5321,"outip":"124.202.193.26"},{"ip":"58.218.200.223","port":5873,"outip":"42.53.91.144"},{"ip":"58.218.200.223","port":2860,"outip":"39.67.238.8"},{"ip":"58.218.200.227","port":7498,"outip":"125.111.249.49"},{"ip":"58.218.200.227","port":8471,"outip":"182.84.179.112"},{"ip":"58.218.200.225","port":2377,"outip":"223.80.102.234"},{"ip":"58.218.200.227","port":9054,"outip":"120.33.149.187"},{"ip":"58.218.200.226","port":5117,"outip":"111.179.238.76"},{"ip":"58.218.200.228","port":8102,"outip":"113.121.86.123"},{"ip":"58.218.200.226","port":9019,"outip":"182.84.179.56"},{"ip":"58.218.200.225","port":4078,"outip":"120.239.25.133"},{"ip":"58.218.200.225","port":7593,"outip":"111.37.186.32"},{"ip":"58.218.200.228","port":6336,"outip":"49.85.145.69"},{"ip":"58.218.200.223","port":5641,"outip":"101.72.133.12"},{"ip":"58.218.200.227","port":6445,"outip":"180.117.43.114"},{"ip":"58.218.200.223","port":5198,"outip":"112.111.185.29"},{"ip":"58.218.200.225","port":7554,"outip":"223.74.14.68"}]}'
# ip_response = json.loads(s)
# ipList = ip_response["data"]
# print(ipList)
# for i in ipList:
#     ip = i["ip"]
#     port = i["port"]
#     ip_port = str(ip) + ":" + str(port)
#     ip_cache.append(ip_port)
# print(ip_cache)
# proxies["http"] = ip_cache[random.randint(0, len(ip_cache)-1)]
# print(proxies)
