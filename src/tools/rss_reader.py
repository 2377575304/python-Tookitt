import random

class RSSReader:
    """RSS阅读器 - 聚合多个订阅源并高亮显示（演示）"""
    def execute(self, feed_urls=None):
        if not feed_urls:
            return "请提供RSS订阅源，多个用逗号分隔"
        feeds = [f.strip() for f in str(feed_urls).replace('，', ',').split(',') if f.strip()]
        # 实际可用feedparser库，这里演示
        return '\n'.join([f"{url}: 最新5条新闻（演示）" for url in feeds])
