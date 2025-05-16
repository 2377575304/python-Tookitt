class TorrentInfoParser:
    """Torrent种子解析器 - 提取种子文件信息"""
    def execute(self, torrent_path=None):
        print(f"[TorrentInfoParser] 解析种子: {torrent_path}")
        return {"name": "演示种子", "files": ["file1.mkv", "file2.mp4"]}
