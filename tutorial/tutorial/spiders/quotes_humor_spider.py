import scrapy

class HumorQuotes(scrapy.Spider):
    name = "humor_quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag:
            url = url + 'tag/' + tag

        yield scrapy.Request(url, callback=self.parse)

    
    def parse(self, response):
        for quote in response.css("div.quote"):
            quote_text = quote.css('span.text::text').get()
            quote_author = quote.css('small.author::text').get()

            yield {
                'text': quote_text,
                'author': quote_author
            }


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)