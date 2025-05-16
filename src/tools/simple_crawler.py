class SimpleCrawler:
    """简易爬虫框架 - 抓取指定网站的数据"""
    def execute(self, url=None, rules=None):
        print(f"[SimpleCrawler] 爬取网站: {url}，规则: {rules}")
        return "网站数据已抓取（演示）"
