import scrapy
from amazon.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
    name = "AmazonDeals"
    # allowed_domains = ["amazon.com"]
    page_number = 2
    #Use working product URL below
    start_urls = [
        'https://www.amazon.in/s?k=Mobiles&rh=n%3A1389401031&ref=nb_sb_noss'
        ]
    
    def parse(self, response):
        items = AmazonItem()
        title = response.css('.a-size-medium::text').extract()
        price = response.css('.a-price-whole::text').extract()
        
        items['title'] = title
        items['price'] = price
        
        next_page = "https://www.amazon.in/s?k=Mobiles&i=electronics&rh=n%3A1389401031&page="+ str(AmazonProductSpider.page_number) +"&qid=1621106266&ref=sr_pg_2"
        
        if AmazonProductSpider.page_number <= 3 :
            AmazonProductSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)
        
        
        yield items