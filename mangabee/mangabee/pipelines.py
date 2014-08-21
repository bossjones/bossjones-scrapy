# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


### class MangabeePipeline(object):
###     def process_item(self, item, spider):
###         return item

### import scrapy
### from scrapy.contrib.pipeline.images import ImagesPipeline
### from scrapy.exceptions import DropItem
###
### class MyImagesPipeline(ImagesPipeline):
###
###     def get_media_requests(self, item, info):
###         for image_url in item['image_urls']:
###             yield scrapy.Request(image_url)
###
###     def item_completed(self, results, item, info):
###         image_paths = [x['path'] for ok, x in results if ok]
###         if not image_paths:
###             raise DropItem("Item contains no images")
###         item['image_paths'] = image_paths
###         return item
###

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from PIL import Image
from cStringIO import StringIO
import re

class MangaBeeImagesPipeline(ImagesPipeline):

    CONVERTED_ORIGINAL = re.compile('^full/[0-9,a-f]+.jpg$')

    # name information coming from the spider, in each item
    # add this information to Requests() for individual images downloads
    # through "meta" dict
    def get_media_requests(self, item, info):
        print "get_media_requests"
        return [Request(x, meta={'image_names': item["image_name"]})
                for x in item.get('image_urls', [])]

    # this is where the image is extracted from the HTTP response
    def get_images(self, response, request, info):
        print "get_images"

        for key, image, buf, in super(MangaBeeImagesPipeline, self).get_images(response, request, info):
            if self.CONVERTED_ORIGINAL.match(key):
                key = self.change_filename(key, response)
            yield key, image, buf

    def change_filename(self, key, response):
        return "/Users/malcolm/aot/full/%s.jpg" % response.meta['image_name'][0]
