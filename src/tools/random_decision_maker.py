class RandomDecisionMaker:
    """随机决定工具 - 帮你做选择（抛硬币等）"""
    def execute(self, options=None):
        print(f"[RandomDecisionMaker] 随机决定: {options}")
        return options[0] if options else None
