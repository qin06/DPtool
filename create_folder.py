import os
import json

# 在脚本中定义 JSON 格式的文件夹结构
folders_json = """
{
  "folders": [
    "audio/convert",
    "audio/cut",
    "audio/merged",
    "audio/mix",
    "video/convert",
    "video/separate",
    "video/merged",
    "document/images",
    "temp"
  ]
}
"""

# 解析 JSON 数据
data = json.loads(folders_json)

# 获取需要创建的文件夹列表
folders_to_create = data.get("folders", [])

# 遍历文件夹列表并创建
for folder in folders_to_create:
    try:
        os.makedirs(folder, exist_ok=True)
        print(f"文件夹 '{folder}' 创建成功！")
    except Exception as e:
        print(f"创建文件夹 '{folder}' 时出错: {e}")
