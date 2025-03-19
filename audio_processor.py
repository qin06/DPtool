import subprocess


class AudioEditor:
    def __init__(self, output_audio=None, input_audio=None):
        self.input_audio = input_audio
        self.output_audio = output_audio
        self.ffmpeg_path = 'ffmpeg'

    # 转换音频格式
    def convert_audio(self):
        command = [
            self.ffmpeg_path,
            '-i', self.input_audio,
            self.output_audio
        ]
        subprocess.run(command, check=True)

    # 合并音频文件
    def merge_audio(self, input_files):
        # 创建一个临时文件列表
        with open('temp/temp_list.txt', 'w') as f:
            for file in input_files:
                f.write(f"file '{file}'\n")

        command = [
            self.ffmpeg_path,
            '-f', 'concat',
            '-i', './temp/temp_list.txt',
            '-acodec', 'copy',
            '-y',  # 覆盖输出文件
            self.output_audio
        ]
        subprocess.run(command, check=True)
        # 使用示例 merge_audio(['input1.mp3', 'input2.mp3', 'input3.mp3'])
        # 清空 temp_list.txt 文件
        """with open('temp_list.txt', 'w') as f:
            f.write('')"""

    # 音频混流
    def mix_audio(self, input_files):
        inputs = []
        for i, file in enumerate(input_files):
            inputs.extend(['-i', file])

        command = [
            self.ffmpeg_path,
            *inputs,
            '-filter_complex', f'amix=inputs={len(input_files)}:duration=longest',
            self.output_audio
        ]
        subprocess.run(command, check=True)
        # 使用示例 mix_audio(['audio1.mp3', 'audio2.mp3'])

    # 剪切音频文件
    def clip_audio(self, start_time, end_time):
        command = [
            self.ffmpeg_path,
            '-i', self.input_audio,
            '-ss', start_time,
            '-to', end_time,
            '-c:a', 'pcm_s16le',
            '-q:a', '0',
            self.output_audio
        ]
        subprocess.run(command, check=True)
        """
        常用音频编码器及其特点
        1. MP3 (libmp3lame)
           - 特点：广泛支持，适用于一般用途，压缩比高，音质较好。
           - 示例命令：ffmpeg -i input.wav -c:a libmp3lame output.mp3

        2. AAC (libfdk_aac)
           - 特点：广泛支持，适用于移动设备和流媒体，音质较好，压缩效率高。
           - 示例命令：ffmpeg -i input.wav -c:a libfdk_aac output.m4a

        3. Opus (libopus)
           - 特点：高效率、低延迟，适用于网络流媒体和语音通信，音质优秀。
           - 示例命令：ffmpeg -i input.wav -c:a libopus output.opus

        4. Vorbis (libvorbis)
           - 特点：开源、无损，适用于高质量音频存储。
           - 示例命令：ffmpeg -i input.wav -c:a libvorbis output.ogg

        5. FLAC (flac)
           - 特点：无损音频，压缩比适中，音质无损。
           - 示例命令：ffmpeg -i input.wav -c:a flac output.flac

        6. WAV (pcm_s16le)
           - 特点：未压缩的音频格式，音质无损，文件较大。
           - 示例命令：ffmpeg -i input.wav -c:a pcm_s16le output.wav

        7. Dolby Digital (ac3)
           - 特点：适用于多声道音频，常用于电影和电视。
           - 示例命令：ffmpeg -i input.wav -c:a ac3 output.ac3

        8. Dolby Digital Plus (eac3)
           - 特点：改进的 Dolby Digital，支持更高的比特率。
           - 示例命令：ffmpeg -i input.wav -c:a eac3 output.eac3

        9. Windows Media Audio (wmav2)
           - 特点：适用于 Windows 平台。
           - 示例命令：ffmpeg -i input.wav -c:a wmav2 output.wma
        """
