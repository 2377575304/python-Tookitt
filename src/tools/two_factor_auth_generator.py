class TwoFactorAuthGenerator:
    """双因素认证生成器 - 生成2FA验证码"""
    def execute(self, secret=None):
        print(f"[TwoFactorAuthGenerator] 2FA生成: {secret}")
        return "123456"
