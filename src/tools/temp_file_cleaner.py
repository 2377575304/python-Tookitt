import os
import shutil


class TempFileCleaner:
    """临时文件清理工具 - 自动清理系统/指定目录下的临时文件"""
    def execute(self, folder_path=None):
        # Windows下默认清理%TEMP%目录
        if not folder_path:
            folder_path = os.environ.get('TEMP')
        if not folder_path or not os.path.exists(folder_path):
            return "未找到临时文件夹"
        try:
            count = 0
            for root, dirs, files in os.walk(folder_path):
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                        count += 1
                    except Exception:
                        continue
                for d in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, d), ignore_errors=True)
                    except Exception:
                        continue
            return f"已清理{count}个临时文件"
        except Exception as e:
            return f"清理失败: {e}"
