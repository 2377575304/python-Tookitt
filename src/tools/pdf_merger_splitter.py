import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PDFMergerSplitter:
    """PDF合并拆分器 - 合并或拆分PDF文档
    合并: pdf_list=逗号分隔文件, output_path=输出
    拆分: pdf_path=单文件, output_folder=输出文件夹
    """
    def merge(self, pdf_list=None, output_path=None):
        if not pdf_list or not output_path:
            return "请提供pdf_list（逗号分隔）和output_path"
        files = [f.strip() for f in pdf_list.split(',') if f.strip()]
        merger = PdfMerger()
        try:
            for f in files:
                merger.append(f)
            merger.write(output_path)
            merger.close()
            return f"合并完成，已保存到 {output_path}"
        except Exception as e:
            return f"合并失败: {e}"

    def split(self, pdf_path=None, output_folder=None):
        if not pdf_path or not output_folder:
            return "请提供pdf_path和output_folder"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        try:
            reader = PdfReader(pdf_path)
            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                out_path = os.path.join(output_folder, f"page_{i+1}.pdf")
                with open(out_path, 'wb') as f:
                    writer.write(f)
            return f"拆分完成，共{len(reader.pages)}页，已保存到 {output_folder}"
        except Exception as e:
            return f"拆分失败: {e}"
