import random

class DiceSimulator:
    """骰子模拟器 - 可自定义面数和次数，返回结果列表"""
    def execute(self, sides=6, rolls=1):
        try:
            sides = int(sides)
            rolls = int(rolls)
        except Exception:
            return "参数格式错误"
        if sides < 2 or rolls < 1:
            return "面数需>=2，次数需>=1"
        result = [random.randint(1, sides) for _ in range(rolls)]
        return f"结果：{result}"
