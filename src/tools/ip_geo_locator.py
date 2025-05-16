import random

class IPGeoLocator:
    """IP地理位置查询 - 根据IP显示物理地址（演示）"""
    def execute(self, ip=None):
        if not ip:
            return "请提供IP地址"
        # 实际可用第三方API，这里演示
        city = random.choice(['北京', '上海', '广州', '深圳', '杭州'])
        return f"{ip}：{city}（演示）"
