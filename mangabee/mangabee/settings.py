# -*- coding: utf-8 -*-

# Scrapy settings for mangabee project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mangabee'

SPIDER_MODULES = ['mangabee.spiders']
NEWSPIDER_MODULE = 'mangabee.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mangabee (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
#ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
ITEM_PIPELINES = ['mangabee.pipelines.MangaBeeImagesPipeline']
IMAGES_STORE = '/Users/malcolm/aot'
