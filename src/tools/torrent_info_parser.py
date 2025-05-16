import random


class TorrentInfoParser:
    """Torrent种子解析器 - 提取种子文件信息（演示）"""
    def execute(self, torrent_path=None):
        if not torrent_path:
            return "请提供种子文件路径"
        # 实际可用bencodepy等库，这里演示
        files = [f"file{i}.mkv" for i in range(1, 4)]
        return f"种子文件包含：{', '.join(files)}（演示）"
