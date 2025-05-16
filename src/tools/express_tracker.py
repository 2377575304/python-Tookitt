import requests

class ExpressTracker:
    """快递单号追踪 - 聚合查询多家物流（演示：返回单号）"""
    def execute(self, tracking_number=None):
        if not tracking_number:
            return "请提供快递单号"
        # 实际应用可接入快递100等API，这里演示返回单号
        return f"快递单号 {tracking_number}：运输中（演示）"
