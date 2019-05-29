# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class TestSpiderSpider(scrapy.Spider):
    name = "mafengwo"
    allowed_domains = ["www.mafengwo.cn"]

    def start_requests(self):
        script = """
                      splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
                      splash:go(args.url)
                      splash:wait(5)
                      return {html=splash:html()}
                    end
                """
        yield SplashRequest('https://myip.ipip.net/', args={'wait': 2, "lua_source": script, 'proxy': "http://intramirror:intra123@114.67.89.237:20700"})

    def parse(self, response):
        print(response.text)




