import subprocess


class VideoEditor:
    def __init__(self, input_path=None, output_path=None):
        self.input_path = input_path
        self.output_path = output_path
        self.ffmpeg_path = "ffmpeg"

    # 音频分离
    def extract_audio(self, output_audio_file):
        command = [
            self.ffmpeg_path,
            "-i", self.input_path,
            "-vn",
            "-c:a", "pcm_s16le",
            output_audio_file
        ]
        subprocess.run(command)

    # 视频分离
    def extract_video(self, output_video_file):
        command = [
            self.ffmpeg_path,
            "-i", self.input_path,
            "-an",
            "-c:v", "copy",
            output_video_file
        ]
        subprocess.run(command)

    # 音视频合成
    def merge_audio_video(self, video_file, audio_file, start_time="00:00:00"):
        command = [
            self.ffmpeg_path,
            "-i", video_file,
            "-i", audio_file,
            "-c:v", "copy",
            "-c:a", "aac",
            "-ss", start_time,
            "-map", "0:v:0",
            "-map", "1:a:0",
            self.output_path
        ]
        subprocess.run(command)

    # 视频转码
    def convert_video(self):
        command = [
            self.ffmpeg_path,
            "-i", self.input_path,
            "-c:v", "libx264",
            "-c:a", "aac",
            self.output_path
        ]
        subprocess.run(command)

    # 视频截取为gif
    def convert_to_gif(self, width, height):
        command = [
            self.ffmpeg_path,
            "-i", self.input_path,
            "-vf", f"scale={width}:{height}",
            "-f", "gif",
            self.output_path
        ]
        subprocess.run(command)

