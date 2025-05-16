class ExcelProcessor:
    """Excel表格处理器 - 自动合并/拆分Excel文件"""
    def execute(self, file_paths=None, mode='merge', output_path=None):
        print(f"[ExcelProcessor] 执行Excel处理: {file_paths}, 模式={mode}, 输出={output_path}")
        return "Excel处理已完成（演示）"
