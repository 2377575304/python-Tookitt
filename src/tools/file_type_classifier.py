import os
import shutil


class FileTypeClassifier:
    """文件类型分类器 - 按扩展名自动归类文件到子文件夹"""

    def execute(self, folder_path=None):
        if not folder_path:
            return "请提供文件夹路径"
        if not os.path.exists(folder_path):
            return "文件夹不存在"
        count = 0
        for f in os.listdir(folder_path):
            path = os.path.join(folder_path, f)
            if os.path.isfile(path):
                ext = os.path.splitext(f)[-1].lower().replace(".", "") or "other"
                target_dir = os.path.join(folder_path, ext)
                os.makedirs(target_dir, exist_ok=True)
                try:
                    shutil.move(path, os.path.join(target_dir, f))
                    count += 1
                except Exception:
                    continue
        return f"已分类{count}个文件"
