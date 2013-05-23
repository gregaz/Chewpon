from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from publix.items import PublixItem

class PublixSpider(CrawlSpider):
   name = "publix"
   allowed_domains = ["publix.com"]
   start_urls = [
       "http://mobilead.publix.com/publixmobile/Default.aspx?action=browsecategoryl1&storeid=2500144&viewmode=0&cattreeid=5117975",
   ]
   rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        #Rule(SgmlLinkExtractor(allow=('default\.aspx', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(allow=()), callback='parseCoupons'),
    )

   def parseDept(self, response):
       pass
   
   
   
   
   def parseCoupons(self, response):
       #filename = 'test'
       #open(filename, 'wb').write(response.body)
       start = response.body.find('<div id="iphoneline">')
       end = response.body.find('<div id="footerContainer">')

       response_new = response.replace(body=response.body[start:end])
	   
       hxs = HtmlXPathSelector(response_new)
              
       item = PublixItem()
       item['title'] = 			hxs.select("//div[@class='product-title']/text()").extract()
       item['price'] =      	hxs.select("//div[@class='product-deal']/text()").extract()
       item['priceDetails'] =	hxs.select("//div[@class='product-pricequal']/text()").extract()
       item['desc'] =			hxs.select("//div[@class='product-desc']/text()").extract()
       item['expiry'] =			hxs.select("//div[@class='validdate']/text()").extract()
        
       item['link'] = 			response.url
       item['image'] = 			hxs.select("//img/@src").extract()
	          
       return item
