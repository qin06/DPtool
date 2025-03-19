import os
import subprocess
from pdf2image import convert_from_path


class DocumentEditor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.poppler_path = "./poppler/Library/bin"

    def pdf_to_images(self, dpi):
        """
        将 PDF 文件转换为图片
        :param dpi: 图片分辨率
        """
        file_name = os.path.basename(self.input_path)
        name, extension = os.path.splitext(file_name)

        # 将 PDF 转换为图像列表
        images = convert_from_path(self.input_path, dpi=dpi, poppler_path=self.poppler_path)

        # 保存每一页为图片
        for page_num, image in enumerate(images):
            output_path = os.path.join(self.output_path, f"{name}_p{page_num + 1}.png")
            image.save(output_path, 'PNG')
