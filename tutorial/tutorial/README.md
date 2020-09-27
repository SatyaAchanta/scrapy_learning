This project is all about getting hands on experience with scrapy

Link for tutorial: https://docs.scrapy.org/en/latest/intro/tutorial.html

Commands:

    scrapy crawl <spider_name> - Runs our spider

    Selectors To extract data with Scrapy:
    -------------------------------------

        1. scrapy shell <url_inside_single_quotes> for mac
        2. scrapy shell <url_inside_double_quotes> for windows

    response.css('title').getall() - returns list of all elements directly inside title element
    response.css('title::text').get() - returns the first element in the list returned
    response.css('title::text').re(r'Quotes.*') - returns list of elements based on regex
    response.xpath('//span[has-class("text")]/text()').getall() - returns text inside for all the <span> those have class "text"
    response.css('span.score') - returns all the <span> elements with class 'score'
    response.css('li.next a::attr(href)').get() - returns value of a certain element in the DOM

