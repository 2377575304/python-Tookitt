class PDFMergerSplitter:
    """PDF合并拆分器 - 合并或拆分PDF文档"""
    def merge(self, pdf_list=None, output_path=None):
        print(f"[PDFMergerSplitter] 合并PDF: {pdf_list} -> {output_path}")
        return "PDF已合并（演示）"

    def split(self, pdf_path=None, output_folder=None):
        print(f"[PDFMergerSplitter] 拆分PDF: {pdf_path} -> {output_folder}")
        return "PDF已拆分（演示）"
