import os
from PyPDF2 import PdfReader

class PDFTextExtractor:
    """PDF文本提取器 - 从PDF中提取文字内容，支持单文件"""
    def execute(self, pdf_path=None, output_path=None):
        if not pdf_path:
            return "请提供pdf_path"
        if not os.path.exists(pdf_path):
            return "PDF文件不存在"
        try:
            reader = PdfReader(pdf_path)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                return f"提取完成，已保存到 {output_path}"
            return text[:1000] + ('...\n(内容过长已截断)' if len(text) > 1000 else '')
        except Exception as e:
            return f"提取失败: {e}"
