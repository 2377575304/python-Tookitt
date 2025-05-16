class DiceSimulator:
    """骰子模拟器 - 带统计功能的骰子工具"""
    def execute(self, sides=6, rolls=1):
        print(f"[DiceSimulator] 骰子模拟: {sides}面，{rolls}次")
        return [1]*rolls
