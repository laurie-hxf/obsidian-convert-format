## Brief introduce

this [scripts](https://github.com/laurie-hxf/obsidian-convert-format) is use for convert markdown file in obsidian into blog format

mainly move the screenshot into blog file and change the screenshot name into blog format and add Note Properties for the blog

It convert the screenshot name from ![[XXX XXX.png]] into ![alt text](XXXX%20XXXX.png) and search all the screenshot, moving them to blog folder.

## Use

modify the file path

```python
input_document = input("请输入笔记目录名:").strip()

input_file = input("请输入笔记文件名: ").strip()

output_file = "index.md"

post_file = input("请输入blog文件名:").strip()


# 输入和输出目录（请修改为你的路径）

input_directory = "obsidian path"

picture_directory = os.path.join("obsidian path",input_document,"screenshot floder")

output_directory = os.path.join("blog path",post_file)

image_copy_directory = output_directory # 新的文件夹，存放复制的图片
```

use it on shell 

```shell
python "this python file"
```
