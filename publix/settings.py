# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'publix'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['publix.spiders']
NEWSPIDER_MODULE = 'publix.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
    'publix.pipelines.PublixPipeline',
   
]
