import os
import re
import urllib.parse

# 输入和输出目录（请修改为你的路径）
input_directory = "/Users/laurie/Library/Mobile Documents/iCloud~md~obsidian/Documents/计算机/umich"
output_directory = "/Users/laurie/test"

# 确保输出目录存在
os.makedirs(output_directory, exist_ok=True)

# 正则匹配 Obsidian 图片语法 ![[文件名]]
pattern = r"!\[\[(.+?)\]\]"

# 遍历目录中的所有 Markdown 文件
for filename in os.listdir(input_directory):
    if filename.endswith(".md"):
        input_filepath = os.path.join(input_directory, filename)
        output_filepath = os.path.join(output_directory, filename)

        # 读取 Markdown 文件内容
        with open(input_filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # 替换图片语法
        def replace_match(match):
            image_name = match.group(1)  # 获取图片文件名
            encoded_name = image_name.replace(" ", "%20")    # 仅编码空格，保留中文
            return f"![alt text](./{encoded_name})"  # 替换格式

        new_content = re.sub(pattern, replace_match, content)

        # 写入新文件夹
        with open(output_filepath, "w", encoding="utf-8") as file:
            file.write(new_content)

print(f"Markdown 图片格式转换完成！所有修改后的文件已保存到 {output_directory}")
