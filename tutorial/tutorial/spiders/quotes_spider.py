import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

        parsedQuotesFile = 'quotes-text-authors.json'
        with open(parsedQuotesFile, 'w') as f:
            json.dump(self.get_parsed_quotes_and_authors(response), f, indent=4)


    def get_parsed_quotes_and_authors(self, response):
        allQuotes = []

        for quote in response.css("div.quote"):
            quote_text = quote.css('span.text::text').get()
            quote_author = quote.css('small.author::text').get()
            allQuotes.append(dict (text = quote_text, author = quote_author))

        return allQuotes