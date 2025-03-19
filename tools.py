import os
import shutil

from audio_processor import AudioEditor
from video_processor import VideoEditor
from document_processor import DocumentEditor


def get_file_name_and_extension(file_path):
    # 获取文件名
    file_name = os.path.basename(file_path)
    # 分离文件名和后缀
    name, extension = os.path.splitext(file_name)
    return name, extension


############################
def cut_audio(input_audio, start_time, end_time):
    file_name, extension = get_file_name_and_extension(input_audio)
    editor = AudioEditor(input_audio=input_audio,
                         output_audio='./audio/cut/' + file_name + '_cut' + extension)
    editor.clip_audio(start_time, end_time)
    return './audio/cut/' + file_name + '_cut' + extension


def convert_audio(input_audio, extension):
    file_name, e = get_file_name_and_extension(input_audio)
    editor = AudioEditor(input_audio=input_audio, output_audio='./audio/convert/' + file_name + extension)
    editor.convert_audio()
    return './audio/convert/' + file_name + extension


def mix_audio(input_files, extension):
    file_names = os.listdir(input_files)
    absolute_paths = [os.path.abspath(os.path.join(input_files, file_name)) for file_name in file_names]
    absolute_paths.sort()
    name = os.path.splitext(os.path.basename(absolute_paths[0]))[0]
    editor = AudioEditor(output_audio='./audio/mix/' + name + extension)
    editor.mix_audio(input_files=absolute_paths)
    return './audio/mix/' + name + extension


def merge_audio(input_files):
    temp_folder = './temp/'
    for file in input_files:
        shutil.copy2(file, temp_folder)
    file_names = os.listdir(temp_folder)

    name, extension = os.path.splitext(os.path.basename(input_files[0]))
    editor = AudioEditor(output_audio='./audio/merged/' + name + extension)
    editor.merge_audio(input_files=file_names)

    shutil.rmtree(temp_folder)
    os.makedirs(temp_folder, exist_ok=True)

    return './audio/merged/' + name + extension


##################################
def separate_video(input_video):
    file_name, extension = get_file_name_and_extension(input_video)
    editor = VideoEditor(input_path=input_video)
    editor.extract_video(output_video_file='./video/separate/' + file_name + extension)
    editor.extract_audio(output_audio_file='./video/separate/' + file_name + '.m4a')
    return ['./video/separate/' + file_name + extension, './video/separate/' + file_name + '.m4a']


def merge_audio_video(input_video, input_audio, start_time):
    file_name, extension = get_file_name_and_extension(input_video)
    editor = VideoEditor(output_path='./video/merged/' + file_name + extension)
    editor.merge_audio_video(video_file=input_video, audio_file=input_audio, start_time=start_time)
    return './video/merged/' + file_name + extension


def convert_video(input_video, mode='video', extension='.mp4', width=256, height=256):
    file_name, e = get_file_name_and_extension(input_video)
    if mode == 'gif':
        editor = VideoEditor(input_path=input_video, output_path='./video/convert/' + file_name + '.gif')
        editor.convert_to_gif(width=width, height=height)
        return './video/convert/' + file_name + '.gif'
    elif mode == 'video':
        editor = VideoEditor(input_path=input_video, output_path='./video/convert/' + file_name + extension)
        editor.convert_video()
        return './video/convert/' + file_name + extension


##############################################
def pdf_to_images(input_pdf, dpi=300):
    editor = DocumentEditor(input_path=input_pdf, output_path='./document/images/')
    editor.pdf_to_images(dpi=dpi)
    return '转换至'+'./document/images/'
