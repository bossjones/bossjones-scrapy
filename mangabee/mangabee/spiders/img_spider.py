import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
import urlparse
from scrapy.selector import Selector
from IPython.core.debugger import Tracer


class CustomItem(scrapy.Item):
    image_urls = Field()
    image_name = Field()
    images = Field()


class ImageSpider(scrapy.Spider):
    name = "customimg"
    allowed_domains = ["www.mangabee.com"]
    max_page = 2 #58
    start_urls = []
    for i in range(1, max_page):
        manga_url = 'http://www.mangabee.com/Attack_on_Titan_2014/1/%d/' % (i)
        start_urls.append(manga_url)

    # def parse(self, response):
    #     hxs = HtmlXPathSelector(response)
    #     sites = hxs.select('//img')
    #     items = []
    #     for site in sites:
    #         item = CustomItem()
    #         item['image_urls'] = [urlparse.urljoin(response.url, u) for u in site.select('@src').extract()]
    # the name information for your image
    #         item['image_name'] = ['whatever_you_want']
    #         items.append(item)
    #     return items

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src')
        # OLD ONE #sites = sel.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src')
        items = []
        for site in sites:
            item = CustomItem()
            # OLD ONE #item['image_urls'] = [site.extract()]
            # url_array = urlparse.urljoin(response.url, u) for u in site.xpath('@src').extract()
            item['image_urls'] = [site.extract()] #[urlparse.urljoin(response.url, u) for u in site.xpath('@src').extract()[0]]
            item['image_name'] = [response.url.split("/")[-4] + "_" + response.url.split("/")[-3] + "_" + response.url.split("/")[-2] + ".jpg"]
            #item['image_name'] = ["whatever_you_want"]
            items.append(item)
            Tracer()()
        return items
