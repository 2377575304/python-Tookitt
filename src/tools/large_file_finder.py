import os

class LargeFileFinder:
    """大文件查找器 - 找出文件夹下最大的N个文件"""
    def execute(self, folder_path=None, top_n=10):
        if not folder_path:
            return "请提供文件夹路径"
        if not os.path.exists(folder_path):
            return "文件夹不存在"
        try:
            file_sizes = []
            for root, _, files in os.walk(folder_path):
                for f in files:
                    path = os.path.join(root, f)
                    try:
                        size = os.path.getsize(path)
                        file_sizes.append((path, size))
                    except Exception:
                        continue
            file_sizes.sort(key=lambda x: x[1], reverse=True)
            top_files = file_sizes[:int(top_n)]
            result = '\n'.join([f"{os.path.basename(f)}\t{size/1024/1024:.2f}MB" for f, size in top_files])
            return result or "未找到大文件"
        except Exception as e:
            return f"查找失败: {e}"
