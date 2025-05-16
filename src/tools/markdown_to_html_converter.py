import markdown
import os

class MarkdownToHTMLConverter:
    """Markdown转HTML工具 - 支持单文件转换，自动保存结果"""
    def execute(self, md_path=None, html_path=None):
        if not md_path or not html_path:
            return "请提供md_path和html_path"
        if not os.path.exists(md_path):
            return "Markdown文件不存在"
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                text = f.read()
            html = markdown.markdown(text)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html)
            return f"转换完成，已保存到 {html_path}"
        except Exception as e:
            return f"转换失败: {e}"
