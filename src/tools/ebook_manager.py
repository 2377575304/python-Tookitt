import os

class EbookManager:
    """电子书管理工具 - 整理EPUB/MOBI格式书籍到分类文件夹"""
    def execute(self, folder_path=None):
        if not folder_path:
            return "请提供电子书文件夹路径"
        if not os.path.exists(folder_path):
            return "文件夹不存在"
        count = 0
        for f in os.listdir(folder_path):
            path = os.path.join(folder_path, f)
            if os.path.isfile(path):
                ext = os.path.splitext(f)[-1].lower().replace('.', '')
                if ext in ('epub', 'mobi', 'azw3', 'pdf'):
                    target_dir = os.path.join(folder_path, ext)
                    os.makedirs(target_dir, exist_ok=True)
                    try:
                        os.rename(path, os.path.join(target_dir, f))
                        count += 1
                    except Exception:
                        continue
        return f"已整理{count}本电子书"
