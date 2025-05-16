import qrcode

class QRCodeGenerator:
    """二维码生成器 - 将文本/链接转为二维码图片"""
    def execute(self, text=None, output_path=None):
        if not text:
            return "请提供要生成二维码的文本"
        if not output_path:
            output_path = "qrcode.png"
        try:
            img = qrcode.make(text)
            img.save(output_path)
            return f"二维码已生成，保存路径: {output_path}"
        except Exception as e:
            return f"生成失败: {e}"
