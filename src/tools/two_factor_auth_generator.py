import random


class TwoFactorAuthGenerator:
    """双因素认证生成器 - 生成2FA验证码（演示）"""
    def execute(self, secret=None):
        # 实际可用pyotp等库，这里演示
        code = random.randint(100000, 999999)
        return f"当前验证码：{code}（演示）"
