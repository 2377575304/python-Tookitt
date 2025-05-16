import random


class NetworkSpeedTester:
    """网络速度测试器 - 实时监测网络带宽（演示）"""
    def execute(self):
        # 实际可用speedtest-cli等库，这里演示
        download = random.randint(50, 200)
        upload = random.randint(10, 50)
        return f"下行：{download}Mbps，上行：{upload}Mbps（演示）"
