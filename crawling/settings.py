BOT_NAME = "crawling"
SPIDER_MODULES = ["crawling.spiders"]
ITEM_PIPELINES = {"crawling.pipelines.AnalysisPipeline": 300}
