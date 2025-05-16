import os


class DirectoryTreeGenerator:
    """目录树生成器 - 生成文件夹结构的可视化树形图（文本版）"""
    def execute(self, folder_path=None, output_path=None):
        if not folder_path:
            return "请提供文件夹路径"
        if not os.path.exists(folder_path):
            return "文件夹不存在"

        def tree(dir_path, prefix=''):
            lines = []
            files = os.listdir(dir_path)
            for idx, f in enumerate(files):
                path = os.path.join(dir_path, f)
                connector = '└── ' if idx == len(files)-1 else '├── '
                lines.append(prefix + connector + f)
                if os.path.isdir(path):
                    extension = '    ' if idx == len(files)-1 else '│   '
                    lines.extend(tree(path, prefix + extension))
            return lines

        lines = [os.path.basename(folder_path) or folder_path]
        lines += tree(folder_path)
        tree_str = '\n'.join(lines)
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(tree_str)
            return f"目录树已保存到: {output_path}"
        return tree_str
