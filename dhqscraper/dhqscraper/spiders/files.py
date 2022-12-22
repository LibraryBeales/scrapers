import re
import scrapy
import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DhqSpider(CrawlSpider):
    name = 'dhqfiles'
    allowed_domains = ['digitalhumanities.org']
    start_urls = ['http://www.digitalhumanities.org/dhq/vol/16/3/index.html']

    rules = (
            Rule(LinkExtractor(allow = 'index.html')), 
            Rule(LinkExtractor(allow = 'vol'), callback='parse_article'),        
        )

    def parse_article(self, response):
        article = { 
            'xmllink' : response.urljoin(response.xpath('(//div[@class="toolbar"]/a[contains(@href, ".xml")]/@href)[1]').get()),
        }
        yield {'file_urls':[article['xmllink']]}
