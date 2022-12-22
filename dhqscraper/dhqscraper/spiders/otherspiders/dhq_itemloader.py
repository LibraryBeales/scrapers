import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from dhqscraper.items import DhqscraperItem
from scrapy.loader import ItemLoader

class DhqSpider(CrawlSpider):
    name = 'dhq3'
    allowed_domains = ['digitalhumanities.org']
    start_urls = ['http://www.digitalhumanities.org/dhq/vol/16/3/index.html']

    rules = (
            Rule(LinkExtractor(allow = 'index.html')), 
            Rule(LinkExtractor(allow = 'vol'), callback='parse_article'),        
        )

    def parse_article(self, response):
        l =  ItemLoader(item = DhqscraperItem(), selector=response)
        
        l.add_css('title', 'h1.articleText')
        l.add_css('authors', 'div.author a')
        l.add_css('pubinfo' 'div#pubInfo')
        l.add_xpath('xmllink', '(//div[@class="toolbar"]/a[contains(@href, ".xml")]/@href)[1]')
        
        yield l.load_item()
        
        
        #item['title'] = response.css('h1.articleTitle::text').get()
        #item['author'] = response.css('div.author a::text').getall()
        #item['pubinfo'] = response.css('div#pubInfo::text').getall()
        #item['xmllink'] = response.urljoin(response.xpath('(//div[@class="toolbar"]/a[contains(@href, ".xml")]/@href)[1]').get())            
        
        
