import scrapy


class ApartmentSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://dubai.dubizzle.com/property-for-rent/residential/apartmentflat/2015/8/5/huge-4-br-on-a-high-floor-now-available-2/?related_ads=1&back=ZHViYWkuZHViaXp6bGUuY29tL3Byb3BlcnR5LWZvci1yZW50L3Jlc2lkZW50aWFsL2FwYXJ0bWVudGZsYXQv',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.results-list'):
            yield {
                'title': quote.xpath(
                    'div/div/div/div[2]/a/div[2]/div[2]/div/div/div/h2/text()').extract(),
                'place': quote.xpath(
                    'div/div/div/div[2]/a/div[2]/div[2]/div/div/div/div/div/span/text()').extract(),
                'updatetime': quote.xpath(
                    'div/div/div/div[2]/a/div[2]/div[2]/div/div/div/div[2]/text()').extract(),
                
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
