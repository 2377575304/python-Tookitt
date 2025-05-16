import os
from PIL import Image

class ASCIIArtGenerator:
    """ASCII艺术生成器 - 将图片转为ASCII字符画"""
    def execute(self, image_path=None, output_path=None):
        if not image_path:
            return "请提供图片路径"
        if not os.path.exists(image_path):
            return "图片文件不存在"
        chars = "@%#*+=-:. "
        try:
            img = Image.open(image_path).convert('L')
            width, height = img.size
            aspect_ratio = height / width
            new_width = 80
            new_height = int(aspect_ratio * new_width * 0.5)
            img = img.resize((new_width, new_height))
            pixels = img.getdata()
            ascii_str = ""
            for i in range(len(pixels)):
                ascii_str += chars[pixels[i] * len(chars) // 256]
                if (i + 1) % new_width == 0:
                    ascii_str += '\n'
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(ascii_str)
                return f"ASCII字符画已保存到: {output_path}"
            return ascii_str
        except Exception as e:
            return f"生成失败: {e}"
