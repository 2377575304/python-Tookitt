class AnniversaryCountdown:
    """纪念日倒计时 - 计算重要日期剩余时间"""
    def execute(self, target_date=None):
        from datetime import datetime
        print(f"[AnniversaryCountdown] 纪念日倒计时: {target_date}")
        if not target_date:
            return "请提供目标日期，格式如 2025-12-31"
        try:
            # 支持常见日期格式
            for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"):
                try:
                    target = datetime.strptime(target_date, fmt)
                    break
                except ValueError:
                    continue
            else:
                return "日期格式错误，请用 2025-12-31"
            today = datetime(2025, 5, 16)  # 可用 datetime.today() 替换为当前系统日期
            delta = (target - today).days
            if delta > 0:
                return f"还有{delta}天"
            elif delta == 0:
                return "就是今天！"
            else:
                return f"已过去{abs(delta)}天"
        except Exception as e:
            return f"解析日期出错: {e}"
