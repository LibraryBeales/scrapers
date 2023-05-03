import re
import scrapy
import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from dhqscraper.items import DhqscraperItem
from scrapy.loader import ItemLoader

class DhqSpider(CrawlSpider):
    name = 'dhq'
    allowed_domains = ['digitalhumanities.org']
    start_urls = ['http://www.digitalhumanities.org/dhq/vol/16/3/index.html']

    rules = (
            Rule(LinkExtractor(allow = 'index.html')), 
            Rule(LinkExtractor(allow = 'vol'), callback='parse_article'),        
        )
    
    def parse_article(self, response):
        title = response.css('h1.articleTitle').xpath('normalize-space(text())').get(default='').strip()
        author = response.css('div.author a').xpath('normalize-space(text())').getall()
        author = [unidecode.unidecode(i) for i in author]
        year = unidecode.unidecode(response.css('div#pubInfo::text')[0].get())
        volume = unidecode.unidecode(response.css('div#pubInfo::text')[1].get())
        file_url = response.urljoin(response.xpath('(//div[@class="toolbar"]/a[contains(@href, ".xml")]/@href)[1]').get())

        item = DhqscraperItem()
        item['title'] = [title]
        item['author'] = [author]
        item['year'] = [year]
        item['volume'] = [volume]
        item['file_urls'] = [file_url]

        yield item