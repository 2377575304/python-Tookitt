class WeatherQuery:
    """天气预报查询 - 获取实时天气数据"""
    def execute(self, city=None):
        print(f"[WeatherQuery] 天气查询: {city}")
        return "天气数据已获取（演示）"
