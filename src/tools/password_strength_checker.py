import re


class PasswordStrengthChecker:
    """密码强度检测器 - 评估密码安全性，返回弱/中/强"""
    def execute(self, password=None):
        if not password:
            return "请提供密码"
        score = 0
        if len(password) >= 8:
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'\d', password):
            score += 1
        if re.search(r'[^A-Za-z0-9]', password):
            score += 1
        if score <= 2:
            return "弱"
        elif score == 3 or score == 4:
            return "中"
        else:
            return "强"
