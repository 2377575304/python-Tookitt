import random


class RandomQuiz:
    """随机知识问答 - 从题库随机出题"""
    def execute(self, question_bank=None):
        # 演示内置题库
        questions = [
            ("中国的首都是哪座城市？", "北京"),
            ("3的平方是多少？", "9"),
            ("Python的作者是谁？", "Guido van Rossum"),
            ("水的化学式是什么？", "H2O"),
        ]
        if question_bank:
            # 支持自定义题库，格式：题目1|答案1,题目2|答案2
            try:
                pairs = [q.split('|') for q in str(question_bank).split(',') if '|' in q]
                if pairs:
                    questions = pairs
            except Exception:
                pass
        q, a = random.choice(questions)
        return f"题目：{q}\n答案：{a}"
