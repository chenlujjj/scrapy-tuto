import scrapy


class QuotesSpider(scrapy.Spider):
    # name must unique
    name = "quotes"

    # must return an iterable of Requests
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    # parse是处理response的默认回调函数
    # response 是 TextResponse 的实例
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            # shortcut
            yield response.follow(next_page, callback=self.parse)