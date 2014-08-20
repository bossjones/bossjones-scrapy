import scrapy
from mangabee.items import ChapterImageItem
from scrapy.selector import Selector
#from IPython.Debugger import Tracer
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.selector import Selector
# from scrapy.http import HtmlResponse
# from scrapy.http import Request
# from scrapy.contrib.linkextractors import LinkExtractor

# In [3]: response.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src').extract()
# Out[3]: [u'http://i11.mangareader.net/shingeki-no-kyojin/1/shingeki-no-kyojin-1813085.jpg']
# for sel in
# response.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img[src]'):


class MangeBeeImageSpider(scrapy.Spider):
    name = "aot_img"
    max_page = 58
    allowed_domains = ["mangabee.com"]
    start_urls = []
    for i in range(1,max_page):
        manga_url = 'http://www.mangabee.com/Attack_on_Titan_2014/1/%d/' % (i)
        start_urls.append(manga_url)

    #print start_urls
    # start_urls = [
    #     "http://www.mangabee.com/Attack_on_Titan_2014/1/" # http://www.mangabee.com/Attack_on_Titan_2014/1/1/
    # ]

    ### def start_requests(self):
    ###     for i in range(1, self.max_page):
    ###         yield Request('http://www.mangabee.com/Attack_on_Titan_2014/1/%d/' % i,
    ###                 meta={'index':i},
    ###                 callback=self.parse_imgs)

    def parse(self, response):
        #for sel in response.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src'):
      sel = Selector(response)
      sites = sel.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src')
      #Tracer()
      items = []
      for site in sites:
        item = ChapterImageItem()
      #image_array = response.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src').extract()
        #item['page_num'] = response.url.split("/")[-2]
        #item['image'] = response.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src').extract()
        item['image'] = site.extract()
        items.append(item)

      return items

        # Returns array with results
        # image_array = response.xpath('//*[@id="sct_content"]/div/div[2]/div[2]/img/@src').extract()
        # returns actual image url
        # image = image_array[0]
        # yield image
