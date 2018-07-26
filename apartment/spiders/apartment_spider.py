import scrapy


class ApartmentSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://dubai.dubizzle.com/en/property-for-rent/residential/apartmentflat'
        ]
        for page in range(1, 40, 1):
            urls.append('https://dubai.dubizzle.com/en/property-for-rent/residential/apartmentflat/?page=' + str(page))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.results-list'):
            yield {
                # 'title': quote.xpath(
                #     'div/div/div/div[2]/a/div[2]/div[2]/div/div/div/h2/text()').extract(),
                # 'place': quote.xpath(
                #     'div/div/div/div[2]/a/div[2]/div[2]/div/div/div/div/div/span/text()').extract(),
                # 'updatetime': quote.xpath(
                #     'div/div/div/div[2]/a/div[2]/div[2]/div/div/div/div[2]/text()').extract(),
                # 'place': quote.xpath(
                #     '//*[contains(concat( " ", @class, " " ), concat( " ", "place", " " ))]/h2/text()').extract(),

                'title': quote.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "en", " " ))]/text()').extract(),
                'place': quote.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "place", " " ))]/span/text()').extract(),
                'updatetime': quote.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "timeago", " " ))]/text()').extract(),
                'price': quote.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "price", " " ))]/text()').extract(),
                # 'logo': quote.xpath('//img/src').extract(),
                'photocount': quote.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "count_value", " " ))]/text()').extract(),

            }

            next_page = response.css('li.next a::attr("href")').extract()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
