import random
import string


class PasswordGenerator:
    """密码生成器 - 生成高强度随机密码，支持自定义长度和是否包含符号"""

    def execute(self, length=16, use_symbols=True):
        try:
            length = int(length)
        except Exception:
            length = 16
        if length < 6:
            return "密码长度建议不少于6位"
        chars = string.ascii_letters + string.digits
        if str(use_symbols).lower() in ('1', 'true', 'yes', 'y', '是'):
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
