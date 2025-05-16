import os
import shutil

class FolderSyncTool:
    """文件夹同步工具 - 双向同步两个文件夹内容（仅文件名和内容，演示版）"""
    def execute(self, folder1=None, folder2=None):
        if not folder1 or not folder2:
            return "请提供两个文件夹路径"
        if not os.path.exists(folder1) or not os.path.exists(folder2):
            return "有文件夹不存在"
        count = 0
        # 简单同步：将folder1中folder2没有的文件复制过去，反之亦然
        for src, dst in [(folder1, folder2), (folder2, folder1)]:
            for f in os.listdir(src):
                src_path = os.path.join(src, f)
                dst_path = os.path.join(dst, f)
                if os.path.isfile(src_path) and not os.path.exists(dst_path):
                    try:
                        shutil.copy2(src_path, dst_path)
                        count += 1
                    except Exception:
                        continue
        return f"同步完成，共复制{count}个文件"
