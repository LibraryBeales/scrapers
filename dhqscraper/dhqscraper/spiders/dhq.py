import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DhqSpider(CrawlSpider):
    name = 'dhq1'
    allowed_domains = ['digitalhumanities.org']
    start_urls = ['http://www.digitalhumanities.org/dhq/vol/16/3/index.html']

    rules = (
            Rule(LinkExtractor(allow = 'index.html')), 
            Rule(LinkExtractor(allow = 'vol'), callback='parse_article'),        
        )

    def parse_article(self, response):
        yield { 
            'title' : response.css('h1.articleTitle::text').get().strip().replace('\n', ' ').replace('\t',''),
            'author1' : response.css('div.author a::text').getall(),
            'year' : response.css('div#pubInfo::text')[0].get(),
            'volume' : response.css('div#pubInfo::text')[1].get(),
            'xmllink' : response.urljoin(response.xpath('(//div[@class="toolbar"]/a[contains(@href, ".xml")]/@href)[1]').get()),            
        }

    
