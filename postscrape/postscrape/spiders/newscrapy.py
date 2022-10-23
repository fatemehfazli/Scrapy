import scrapy

class ZoomSpider(scrapy.Spider):
    name = 'zoom'
    page_number = 2
    start_urls=["https://www.zoomg.ir/page/1/"]
    # start_urls=["https://www.zoomg.ir/"]
    custom_settings = {'FEED_URI': 'myspider.csv'}

    def parse(self, response):
        for article in response.css('div.boxWrapper'):
            title = 'div.Contents > h3 > a ::text'
            author = 'ul.inline-block > li > a ::text'
            date = 'ul.inline-block > li:nth-child(2) ::text'
            summary = 'div.Contents > p ::text'
            img = ' div.imgContainer > a > img::attr(src)'
            yield{
                "title": article.css(title).extract_first(),
                "author": article.css(author).extract_first(),
                "date": article.css(date).extract_first(),
                "summary": article.css(summary).extract_first(),
                "img": article.css(img).extract_first(),
            }
            next_page = 'https://www.zoomg.ir/page/'+ str(ZoomSpider.page_number) + '/'
            if ZoomSpider.page_number < 10:
                ZoomSpider.page_number +=1
                yield response.follow(next_page, callback=self.parse)






                