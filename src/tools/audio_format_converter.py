from pydub import AudioSegment
import os

class AudioFormatConverter:
    """音频格式转换器 - MP3/WAV等格式互转，支持批量转换文件夹下所有音频文件"""
    def execute(self, folder_path=None, src_format=None, dst_format=None):
        if not folder_path or not src_format or not dst_format:
            return "请提供文件夹路径、源格式(src_format)、目标格式(dst_format)"
        if not os.path.exists(folder_path):
            return "文件夹不存在"
        src_format = src_format.lower().replace('.', '')
        dst_format = dst_format.lower().replace('.', '')
        files = [f for f in os.listdir(folder_path) if f.lower().endswith('.'+src_format)]
        if not files:
            return f"未找到.{src_format}文件"
        out_dir = os.path.join(folder_path, f"converted_{dst_format}")
        os.makedirs(out_dir, exist_ok=True)
        count = 0
        for f in files:
            try:
                audio = AudioSegment.from_file(os.path.join(folder_path, f), format=src_format)
                out_name = os.path.splitext(f)[0] + '.' + dst_format
                out_path = os.path.join(out_dir, out_name)
                audio.export(out_path, format=dst_format)
                count += 1
            except Exception as e:
                return f"转换失败: {f}, 错误: {e}"
        return f"共转换{count}个文件，已保存到: {out_dir}"
