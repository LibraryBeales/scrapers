# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
'''import sqlite3

class DhqscraperPipeline:
    def __init__(self):
        self.con = sqlite3.connect('dhqdb')
        self.cur = self.con.cursor()
        
    def create_table(self):
            
      
    def process_item(self, item, spider):
        return item
'''