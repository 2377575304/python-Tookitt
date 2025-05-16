from pydub import AudioSegment
import os

class AudioEditor:
    """音频剪辑工具 - 剪切/合并音频文件
    mode: 'cut'（剪切）或 'concat'（合并）
    剪切时 audio_paths 传单个文件，需参数 start_ms, end_ms
    合并时 audio_paths 传多个文件（逗号分隔）
    """
    def execute(self, audio_paths=None, mode=None, output_path=None, start_ms=None, end_ms=None):
        if not audio_paths or not mode or not output_path:
            return "请提供音频路径、模式（cut/concat）和输出路径"
        try:
            if mode == 'cut':
                audio = AudioSegment.from_file(audio_paths)
                s = int(start_ms) if start_ms else 0
                e = int(end_ms) if end_ms else len(audio)
                cut_audio = audio[s:e]
                cut_audio.export(output_path, format=output_path.split('.')[-1])
                return f"剪切完成，已保存到 {output_path}"
            elif mode == 'concat':
                files = [p.strip() for p in audio_paths.split(',') if p.strip()]
                combined = AudioSegment.empty()
                for f in files:
                    combined += AudioSegment.from_file(f)
                combined.export(output_path, format=output_path.split('.')[-1])
                return f"合并完成，已保存到 {output_path}"
            else:
                return "mode 仅支持 cut 或 concat"
        except Exception as e:
            return f"音频处理失败: {e}"
