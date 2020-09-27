import scrapy

class AllQuotes(scrapy.Spider):
    name = "allquotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get()
            }

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            # we can also replace scrapy.Request with response.follow
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
