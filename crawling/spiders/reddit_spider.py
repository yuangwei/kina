# project_name/spiders/reddit_spider.py
import scrapy

class RedditSpider(scrapy.Spider):
    name = "reddit"
    start_urls = [f"https://www.reddit.com/r/{subreddit}/"]

    def parse(self, response):
        yield {
            "url": response.url,
            "html": response.text,
        }

        next_page = response.css("a.next-button::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
