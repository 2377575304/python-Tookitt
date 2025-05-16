import requests

class WeatherQuery:
    """天气预报查询 - 获取实时天气数据（演示：返回城市名）"""
    def execute(self, city=None):
        if not city:
            return "请提供城市名"
        # 实际应用可接入和风天气、OpenWeather等API，这里演示返回城市名
        return f"{city}：晴，25℃，微风（演示）"
