import requests
import json
from lxml import etree
import datetime
from pymongo import MongoClient


class SinaSpider(object):

    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        self.url = 'https://tech.sina.com.cn/internet/'

    def parse_url(self,url):
        #print(url)
        response = requests.get(url,headers = self.headers)
        # print(response.content.decode())
        return response.content.decode()

    def get_content_list(self,html_str):
        html = etree.HTML(html_str)
        content_list =[]
        li_list = html.xpath('//div[contains(@class,"zggdt-module")]/ul/li')
        for li in li_list:
            item = dict()
            item['url'] = li.xpath('./a/@href')
            item['title'] = li.xpath('.//a/text()')
            content_list.append(item)
        return content_list


    def save_content(self,content_list):
        client = MongoClient(host='127.0.0.1',port=27017)
        formatted_today = datetime.date.today().strftime('%y%m%d')
        collection = client['news']['news_{}'.format(formatted_today)]
        collection.insert_many(content_list)


    def run(self):
        html_str = self.parse_url(self.url)
        content_list = self.get_content_list(html_str)
        self.save_content(content_list)
        # print(content_list)


if __name__ == '__main__':
    s = SinaSpider()
    s.run()
