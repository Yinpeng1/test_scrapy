# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from urllib.parse import unquote
import zlib
import gzip
import time
import requests
# print(unquote('https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18107698208687623114_1559015067800&params=%7B%22type%22%3A0%2C%22objid%22%3A0%2C%22page%22%3A4%2C%22ajax%22%3A1%2C%22retina%22%3A0%7D&_=1559016005577'))

# data = gzip.decompress(b"\u3010\u5e74\u540e\u89e3\u95f7\ud83e\udd32\u3011\u5b81\u9759\u4e0e\u55a7\u56a3\uff0c\u6b65\u5165\u6f33\u5dde\uff0c\u63a2\u7d22\u672a\u77e5\u7684\u571f\u697c\u5473\u9053\u2014")
# print(data)
# print(time.time())

# print("\u3010\u5e74\u540e\u89e3\u95f7\u3011")