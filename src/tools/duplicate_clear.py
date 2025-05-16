import os
import shutil
import hashlib

class ToolA:
    """重复文件清理工具 - 查找并删除文件夹下的重复文件（按内容哈希）"""
    def execute(self, folder_path=None):
        if not folder_path:
            return "请提供文件夹路径"
        if not os.path.exists(folder_path):
            return "文件夹不存在"
        hashes = {}
        duplicates = []
        for root, _, files in os.walk(folder_path):
            for f in files:
                path = os.path.join(root, f)
                try:
                    with open(path, 'rb') as file:
                        file_hash = hashlib.md5(file.read()).hexdigest()
                    if file_hash in hashes:
                        duplicates.append(path)
                    else:
                        hashes[file_hash] = path
                except Exception:
                    continue
        for file in duplicates:
            try:
                os.remove(file)
            except Exception:
                continue
        return f"共清理{len(duplicates)}个重复文件" if duplicates else "未发现重复文件"