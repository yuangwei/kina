from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawling.utils.parser import parse_html
from crawling.utils.llm import chain

def crawl_and_analyze(subreddit):
    process = CrawlerProcess(get_project_settings())
    process.crawl("reddit", subreddit=subreddit)
    process.start()

    # Assuming the spider yields a dictionary with 'url' and 'html' keys
    for item in items:
        topics = parse_html(item["html"])
        text = "\n".join([t["title"] + "\n" + "\n".join(t["comments"]) for t in topics])
        opportunities = chain.run(text)
        yield {
            "url": item["url"],
            "opportunities": opportunities,
        }

if __name__ == "__main__":
    subreddit = "SaaS"
    for analysis in crawl_and_analyze(subreddit):
        print(f"URL: {analysis['url']}")
        for opportunity in analysis["opportunities"]:
            print(f"SaaS Opportunity: {opportunity['opportunity']}")
            print(f"Description: {opportunity['description']}")
            print(f"Supporting Evidence:")
            for evidence in opportunity["evidence"]:
                print(f"- {evidence}")
            print()