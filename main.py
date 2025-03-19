import gradio as gr
import tools


def audio():
    """创建音频处理页面"""
    with gr.Tab("音频剪切"):
        with gr.Row():
            file_input = gr.Audio(label="上传音频",
                                  type="filepath")
            with gr.Tab("剪切区间"):
                start_time = gr.Textbox(value='00:00:00', label="Start Time (HH:MM:SS)")
                end_time = gr.Textbox(value='00:00:00', label="End Time (HH:MM:SS)")
        process_button = gr.Button("剪切")
        output_box = gr.Textbox(label="处理结果", interactive=False)

        process_button.click(
            fn=tools.cut_audio,
            inputs=[file_input, start_time, end_time],
            outputs=output_box
        )

    with gr.Tab("格式转换"):
        with gr.Row():
            file_input = gr.Audio(label="上传音频", type="filepath")
            extension = gr.Dropdown(
                [".mp3", ".m4a", ".wav", ".ogg", ".aac", ".wma", ".flac", ".alac", ".opus", ".aiff", ".au", ".amr",
                 ".dts", ".ac3", ".eac3", ".mp2"], label="目标格式", allow_custom_value=True)
        process_button = gr.Button("转换")
        output_box = gr.Textbox(label="处理结果", interactive=False)

        process_button.click(
            fn=tools.convert_audio,
            inputs=[file_input, extension],
            outputs=output_box
        )

    with gr.Tab("音频混合"):
        with gr.Row():
            file_inputs = gr.Textbox(label="音频文件夹路径", lines=3, placeholder="D:/audio/")
            extension = gr.Dropdown(
                [".mp3", ".m4a", ".wav", ".ogg", ".aac", ".wma", ".flac", ".alac", ".opus", ".aiff", ".au", ".amr",
                 ".dts", ".ac3", ".eac3", ".mp2"], label="目标格式", allow_custom_value=True)
        process_button = gr.Button("混合")
        output_box = gr.Textbox(label="处理结果", interactive=False)

        process_button.click(
            fn=tools.mix_audio,
            inputs=[file_inputs, extension],
            outputs=output_box
        )

    with gr.Tab("音频拼接"):
        file_list_state = gr.State(value=[])
        with gr.Row():
            with gr.Group():
                new_file_input = gr.Textbox(label="新的文件路径", placeholder="例如: D:/audio/audio.mp3")
                add_button = gr.Button("添加文件路径")
            with gr.Group():
                file_list_display = gr.Textbox(label="音频文件路径列表", interactive=False, max_lines=5)

        process_button = gr.Button("拼接")
        output_box = gr.Textbox(label="处理结果", interactive=False)

        def add_file(new_file, current_list):
            """
            添加新的文件路径到列表
            :param new_file: 新的文件路径
            :param current_list: 当前文件路径列表
            :return: 更新后的文件路径列表, 更新后的显示字符串, 空字符串用于清空输入框
            """
            if new_file:  # 确保新文件路径不为空
                current_list.append(new_file)
            print(new_file)
            # 将列表转换为字符串以便在 Textbox 中显示
            list_str = "\n".join([path for path in current_list])
            return current_list, list_str, ""

        add_button.click(
            add_file,
            inputs=[new_file_input, file_list_state],
            outputs=[file_list_state, file_list_display, new_file_input]
        )
        process_button.click(
            fn=tools.merge_audio,
            inputs=[file_list_state],
            outputs=output_box
        )


def video():
    """创建视频处理页面"""
    with gr.Tab("音视频分离"):
        with gr.Row():
            file_input = gr.Video(label="上传视频")
        process_button = gr.Button("分离")
        output_box = gr.Textbox(label="处理结果", interactive=False)
        process_button.click(
            fn=tools.separate_video,
            inputs=[file_input],
            outputs=output_box
        )

    with gr.Tab("音视频合成"):
        with gr.Row():
            video_input = gr.Video(label="上传视频", height=280)
            audio_input = gr.Audio(label="上传音频", type="filepath")
            with gr.Column():
                start_time = gr.Textbox(value='00:00:00', label="音频在视频中的开始时间 (默认为00:00:00)")
                process_button = gr.Button("合成")
        output_box = gr.Textbox(label="处理结果", interactive=False)

        process_button.click(
            fn=tools.merge_audio_video,
            inputs=[video_input, audio_input, start_time],
            outputs=output_box
        )

    with gr.Tab("格式转换"):
        with gr.Row():
            file_input = gr.Video(label="上传视频")
            with gr.Column():
                with gr.Tab("转视频"):
                    extension = gr.Dropdown(
                        [".mp4", ".m4a", ".avi", ".mov", ".flv", ".wmv", ".webm", ".vob", ".m4v", ".mpg", ".mp2",
                         ".mkv",
                         ".mpe", ".mpv", ".ogg", ".ogv", ".m4p", ".m4v"], label="目标格式", allow_custom_value=False)
                    mode_video = gr.State("video")
                    process_button_video = gr.Button("转换")

                with gr.Tab("转GIF"):
                    height = gr.Number(value=256, label="高度")
                    width = gr.Number(value=256, label="宽度")
                    mode_gif = gr.State("gif")
                    process_button_gif = gr.Button("转换")

        output_box = gr.Textbox(label="处理结果", interactive=False)

        process_button_video.click(
            fn=tools.convert_video,
            inputs=[file_input, mode_video, extension],
            outputs=output_box
        )
        process_button_gif.click(
            fn=tools.convert_video,
            inputs=[file_input, mode_gif, width, height],
            outputs=output_box
        )


def document():
    """创建文档处理页面"""
    with gr.Tab("PDF转图片"):
        with gr.Row():
            file_input = gr.File(label="上传PDF文件", type="filepath")
            with gr.Column():
                dpi = gr.Number(value=300, label="分辨率（越大越清晰）")
                process_button = gr.Button("转换")
        output_box = gr.Textbox(label="处理结果", interactive=False)

        process_button.click(
            fn=tools.pdf_to_images,
            inputs=[file_input, dpi],
            outputs=output_box
        )


def create_menu_tabs():
    """创建菜单选项卡"""
    with gr.Tabs():
        with gr.Tab("音频处理"):
            audio()
        with gr.Tab("视频处理"):
            video()
        with gr.Tab("文档处理"):
            document()


def main():
    with gr.Blocks() as demo:
        gr.Markdown("# 文件处理工具")
        create_menu_tabs()

    demo.launch()


if __name__ == "__main__":
    main()
