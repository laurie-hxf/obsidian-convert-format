import os
import re
import shutil
import urllib.parse

# 输入和输出目录（请修改为你的路径）
input_directory = "/Users/laurie/Library/Mobile Documents/iCloud~md~obsidian/Documents/计算机/umich"
picture_directory = "/Users/laurie/Library/Mobile Documents/iCloud~md~obsidian/Documents/计算机/umich/截屏"
output_directory = "/Users/laurie/astro-theme-pure/src/content/blog/deeplearing-L5"
image_copy_directory = "/Users/laurie/astro-theme-pure/src/content/blog/deeplearing-L5"  # 新的文件夹，存放复制的图片

input_file = "Lecture5 Neural Networks.md"
output_file = "index.md"

input_filepath = os.path.join(input_directory, input_file)
output_filepath = os.path.join(output_directory, output_file)

# 确保输出目录存在
os.makedirs(output_directory, exist_ok=True)
os.makedirs(image_copy_directory, exist_ok=True)  # 确保图片文件夹存在

# 正则匹配 Obsidian 图片语法 ![[文件名]]
pattern = r"!\[\[(.+?)\]\]"

# 遍历目录中的所有 Markdown 文件


# 读取 Markdown 文件内容
with open(input_filepath, "r", encoding="utf-8") as file:
    content = file.read()

# 替换图片语法
def replace_match(match):
    image_name = match.group(1)  # 获取图片文件名
    encoded_name = image_name.replace(" ", "%20")    # 仅编码空格，保留中文

    # 复制图片到新的目录
    image_path = os.path.join(picture_directory, image_name)  # 原图片路径
    if os.path.exists(image_path):
        # 目标图片路径
        image_copy_path = os.path.join(image_copy_directory, image_name)
        # 确保目标文件夹存在
        os.makedirs(os.path.dirname(image_copy_path), exist_ok=True)
        # 复制图片
        shutil.copy(image_path, image_copy_path)
    else:
        image_path = os.path.join(input_directory, image_name)
        if os.path.exists(image_path):
            # 目标图片路径
            image_copy_path = os.path.join(image_copy_directory, image_name)
            # 确保目标文件夹存在
            os.makedirs(os.path.dirname(image_copy_path), exist_ok=True)
            # 复制图片
            shutil.copy(image_path, image_copy_path)

    return f"![alt text](./{encoded_name})"  # 替换格式



new_content = re.sub(pattern, replace_match, content)

# 写入新文件夹
with open(output_filepath, "w", encoding="utf-8") as file:
    file.write(new_content)

print(f"Markdown 图片格式转换完成！所有修改后的文件已保存到 {output_directory}")
