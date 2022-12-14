import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DhqSpider(CrawlSpider):
    name = 'dhq'
    allowed_domains = ['digitalhumanities.org']
    start_urls = ['http://www.digitalhumanities.org/dhq/vol/16/3/index.html']

    rules = (
            Rule(LinkExtractor(allow = 'index.html')), 
            Rule(LinkExtractor(allow = 'vol'), callback='parse_xml'),        
        )
    
    def parse_item(self, response):
        yield self.parse_article
        yield self.parse_xmllinks
    
    def parse_xml(self, response):
        xmllink = response.xpath('(//div[@class="toolbar"]/a[contains(@href, ".xml")]/@href)[1]').get()
        yield{
            'file_urls': response.urljoin(xmllink)
            }
    
    def parse_article(self, response):
        yield { 
            'title' : response.css('h1.articleTitle::text').get().strip().replace('\n', ' ').replace('	', ''),
            'author' : response.css('div.author a::text').get().strip(),
            'pubinfo' : response.css('div#pubInfo::text').getall(),
        }
