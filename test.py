import os
import re
import shutil
import urllib.parse
import json
import random

from numpy.lib.recfunctions import join_by

input_document = input("请输入笔记路径:/Users/laurie/Library/Mobile Documents/iCloud~md~obsidian/Documents/").strip()
input_file = input("请输入笔记文件名: ").strip()
output_file = "index.md"
post_file = input("请输入blog文件名:").strip()

# 输入和输出目录（请修改为你的路径）
input_directory = "/Users/laurie/Library/Mobile Documents/iCloud~md~obsidian/Documents"
picture_directory = os.path.join(input_directory,input_document,"截屏")
output_directory = os.path.join("/Users/laurie/astro-theme-pure/src/content/blog",post_file)
image_copy_directory = output_directory # 新的文件夹，存放复制的图片


input_filepath = os.path.join(input_directory,input_document, input_file+".md")
output_filepath = os.path.join(output_directory, output_file)


def get_random_color_by_category(category, filename="/Users/laurie/PycharmProjects/blog_convert/theme_colors.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if category == "全部":
                if "theme_colors" in data and data["theme_colors"]:
                    return random.choice(data["theme_colors"])
            else:
                colors = [color for color in data["theme_colors"] if color["category"] == category]
                if colors:
                    return random.choice(colors)
                else:
                    print(f"未找到色系 '{category}'，请检查输入是否正确")
                    return None
    except FileNotFoundError:
        print("JSON 文件未找到")
        return None


# 运行示例
category = input("请输入bolg主题色色系（绿色系、蓝色系、暖色系、中性色、全部）：")
color = get_random_color_by_category(category)
if color:
    hex_code = color["hex"]
    print(color["name"])
else:
    hex_code = "#FFFFFF"  # 默认白色


text_to_add = f"---\ntitle: '"+input_file+"'\npublishDate: \ndescription: ''\ntags:\n - \n - \nlanguage: 'Chinese'\nheroImage: { src: './', color:'"+hex_code+"'}\n---\n"

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


content = text_to_add + content

new_content = re.sub(pattern, replace_match, content)

# 写入新文件夹
with open(output_filepath, "w", encoding="utf-8") as file:
    file.write(new_content)

print(os.path.abspath(output_filepath))