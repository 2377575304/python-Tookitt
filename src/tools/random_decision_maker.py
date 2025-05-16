import random

class RandomDecisionMaker:
    """随机决定工具 - 帮你做选择（如抛硬币/抽签/选项随机）"""
    def execute(self, options=None):
        if not options:
            return "请提供选项，多个用逗号分隔"
        opts = [x.strip() for x in str(options).replace('，', ',').split(',') if x.strip()]
        if not opts:
            return "无有效选项"
        choice = random.choice(opts)
        return f"随机选择：{choice}"
