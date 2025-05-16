class LargeFileFinder:
    """大文件查找器 - 找出占用空间最大的文件"""
    def execute(self, folder_path=None, top_n=10):
        print(f"[LargeFileFinder] 查找大文件: 文件夹={folder_path}, top_n={top_n}")
        return [f"dummy_file_{i}.dat" for i in range(1, top_n+1)]
