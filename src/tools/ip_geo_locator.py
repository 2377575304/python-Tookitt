class IPGeoLocator:
    """IP地理位置查询 - 根据IP显示物理地址"""
    def execute(self, ip=None):
        print(f"[IPGeoLocator] 查询IP地理位置: {ip}")
        return {"ip": ip, "location": "中国北京（演示）"}
