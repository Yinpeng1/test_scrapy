# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import re
import time
from test_scrapy.items import TestScrapyItem
import urllib
import requests

# 滚动界面爬取列表https://blog.csdn.net/zhao_5352269/article/details/82885166

# function main(splash, args)
# splash: on_request(function(requests)
# request: set_proxy
# {
#     host = "http://intramirror:intra123@114.67.89.237",
#            port = 20700
# }
# js = string.format("document.querySelector('#_j_tn_pagination > a:nth-child(%d)').click();",args.page)
# js = string.format("document.querySelector('#_j_tn_pagination > a.pg-next._j_pageitem').click();", args.page)
#                   splash:runjs(js)
#                   assert(splash:wait(2))
# end
# )
script = """
            function main(splash, args)
                  splash.images_enabled = false  
                  splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
                  assert(splash:go(args.url))
                  assert(splash:wait(1))
                  return splash:html()
         end
         """
script2 = """
            function main(splash, args)
                  splash.images_enabled = false  
                  splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
                  assert(splash:go(args.url))
                  assert(splash:wait(1))
                  js = string.format("document.querySelector('#_j_tn_pagination > a:nth-child(%d)').click();",args.page)
                  splash:runjs(js)
                  assert(splash:wait(2))
                  return splash:html()
         end
         """
script3 = """
            function main(splash, args)
                   splash.images_enabled = false  
                    splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
                    assert(splash:go(args.url))
                    assert(splash:wait(1))
                    js = "document.querySelector('#_j_tn_pagination > a:nth-child(10)').click()"
                    splash:runjs(js)
                    assert(splash:wait(3))
                    js = string.format("document.querySelector('#_j_tn_pagination > a:nth-child(%d)').click();", args.page)
                    splash:runjs(js)
                    assert(splash:wait(2))
                    return {
                        html = splash:html(),
                        png = splash:png(),
                        har = splash:har(),
                  }
         end
         """

class TestSpiderSpider(scrapy.Spider):
    name = "mafengwo"
    allowed_domains = ["www.mafengwo.cn"]

    def start_requests(self):
        for i in range(1, 9):
            yield SplashRequest('https://www.mafengwo.cn/', endpoint='execute', args={'wait': 2, "lua_source": script2, "page": i + 2},
                                # endpoint='render.html',
                                splash_headers={"referer": "https://www.mafengwo.cn/"})
        for j in (10, 12):
            yield SplashRequest('https://www.mafengwo.cn/', endpoint='execute',
                                args={'wait': 2, "lua_source": script3, "page": j + 2 - 4},
                                # endpoint='render.html',
                                splash_headers={"referer": "https://www.mafengwo.cn/"})



    def parse(self, response):
        # print(response.text)
        currentPageNum = response.xpath(
            "//div[@id='_j_tn_pagination']/span[@class='pg-current']/text()").extract_first()
        print("<=========正在爬取第{%s}页面 ========>" % currentPageNum)
        list = response.xpath("//div[@id='_j_tn_content']/div[@class='tn-list']/div[@class='tn-item clearfix']")
        for i in list:
            item = TestScrapyItem()
            if i.xpath("./div[@class='tn-wrapper']/dl/dt/a[@class='tn-from-app']/text()").extract_first() is not None:
                title = i.xpath("./div[@class='tn-wrapper']/dl/dt/a[2]/text()").extract_first()
            else:
                title = i.xpath("./div[@class='tn-wrapper']/dl/dt/a/text()").extract_first()
            if len(i.xpath("./div[@class='tn-wrapper']/dl/dt/a")) != 1:
                url = i.xpath("./div[@class='tn-wrapper']/dl/dt/a[2]/@href").extract_first()
            else:
                url = i.xpath("./div[@class='tn-wrapper']/dl/dt/a/@href").extract_first()

            detail_url = "https://www.mafengwo.cn" + str(url)
            # print("title =====> %s" % title)
            # print("detailUrl =====> %s" % detail_url)
            item["briefTitle"] = title
            item["detailUrl"] = detail_url
            place = i.xpath("./div[@class='tn-wrapper']/div[@class='tn-extra']/span[@class='tn-place']/a[@class='_j_gs_item']/text()").extract_first()
            item["place"] = place
            seeNum = i.xpath("./div[@class='tn-wrapper']/div[@class='tn-extra']/span[@class='tn-nums']/text()").extract_first()
            item["seeNum"] = seeNum
            briefImg = i.xpath("./div[@class='tn-image']/a/img/@src").extract_first()
            item["briefImg"] = briefImg
            likeNum = i.xpath("./div[@class='tn-wrapper']/div[@class='tn-extra']/span[@class='tn-ding']/em/text()").extract_first()
            item["likeNum"] = likeNum
            yield item
        # next_page = int(str(currentPageNum)) + 1
        # if next_page <= 9:
        #     # response.xpath("//a[data-page={page}]".format(page=next_page))
        #     yield SplashRequest('https://www.mafengwo.cn/', endpoint='execute', callback=self.parse,
        #                         args={'wait': 0.5, "lua_source": script2, "page": next_page + 2}, dont_filter=True,
        #                         splash_headers={"referer": "https://www.mafengwo.cn/"})
        # elif 9 < next_page <= 13:
        #     yield SplashRequest('https://www.mafengwo.cn/', endpoint='execute', callback=self.parse,
        #                         args={'wait': 0.5, "lua_source": script3, "page": next_page - 4 + 2}, dont_filter=True,
        #                         splash_headers={"referer": "https://www.mafengwo.cn/"})

            # 详情页
            # yield SplashRequest(detail_url, callback=self.parse_detail,
            #                     args={'wait': 0.5}, dont_filter=True,
            #                     splash_headers={"referer": "https://www.mafengwo.cn/"},
            #                     meta={"data": item})
        # yield item
        # script2 = """
        #               function main(splash)
        #                   splash.images_enabled = false
        #                   assert(splash:go(args.url))
        #                   assert(splash:wait(1))
        #                   local get_dimensions = splash:jsfunc([[
        #                         function () {
        #                             var rect = document.getElementsByClassName('pg-next _j_pageitem')[0].getClientRects()[0];
        #                             return {"x": rect.left, "y": rect.top}
        #                         }
        #                    ]])
        #                   splash:set_viewport_full()
        #                   assert(splash:wait(0.5))
        #                   local dimensions = get_dimensions()
        #                   splash:mouse_click(dimensions.x, dimensions.y)
        #                   splash:wait(0.1)
        #                   return splash:html()
        #         end
        #         """
        # next_page = response.xpath("/div[@class='_j_tn_pagination']/a[@class='pg-next _j_pageitem']")
        # if next_page is not None:
        #     yield SplashRequest(callback=self.parse,
        #                         args={'wait': 0.5, 'lua_source': script2}, dont_filter=True,
        #                         splash_headers={"referer": "https://www.mafengwo.cn/"}, endpoint="execute")
        # 下一页
        # totalPageStr = response.xpath("//div[@id='_j_tn_pagination']/span[@class='count']/text()").extract_first()
        # print("totalPageStr ====> %s" % totalPageStr)
        # reg = re.compile(r'共(.*)页')
        # totalPage = re.findall(reg, repr(totalPageStr))  # 获取字符串中所有匹配的字符串
        # print("totalPage ====> %s" % totalPage[0])
        # currentPageNum = response.xpath("//div[@id='_j_tn_pagination']/span[@class='pg-current']/text()").extract_first()
        # print("currentPageNum ========>%s" % currentPageNum)
        # nextPageNum = int(str(currentPageNum)) + 1
        # currentTime = str(time.time() * 1000).split('.')[0]
        # next_url = 'https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18106270182851686801_1559042985551&params={"type":0,"objid":0,"page": '+str(nextPageNum)+',"ajax":1,"retina":0}&_='+currentTime
        # print("nextUrl ====>%s" % next_url)
        # if int(str(totalPage)) >= currentPageNum:
        #     next_res = requests.get(urllib.parse.urlencode(next_url).encode('utf-8'))
        #     yield print(next_res)

    def parse_detail(self, response):
        # print("text ====>%s", str(response.text))
        # print(response.xpath("//div[@class='_j_titlebg']/div[@class='view_info']/div"))
        item = response.meta["data"]
        detail_title = response.xpath(
            "//div[@class='_j_titlebg']/div[@class='view_info']/div[@class='vi_con']/h1/text()").extract_first()
        print("detail_title =====> %s" % detail_title)
        item["detailTitle"] = detail_title
        yield item
