from datetime import datetime

def generate_markdown_template(title, author, tags, initial_date, update_date):
    """
    生成一个Markdown文件模板字符串。
    
    参数:
        author (str): 文章作者
        initial_date (str): 创建日期
        update_date (str): 更新日期
        title (str): 文章标题
        tags (list of str): 标签列表
    返回:
        str: 包含Markdown元数据的字符串
    """
    # 将标签列表转换为字符串格式
    tags_str = ', '.join([f"[{tag}]" for tag in tags])
    
    template = f"""---
author: [{author}]
date: [{initial_date}]
update: [{update_date}]
title: [{title}]
tags: {tags_str}
---
"""
    return template

# 设置参数
author = "Even"
initial_date = datetime.now().strftime("%Y年%m月%d日")
update_date = datetime.now().strftime("%Y年%m月%d日")
title = "【强化学习】专栏介绍"
tags = ["强化学习,数学原理,实践,简介"]

# 生成Markdown模板
markdown_content = generate_markdown_template(title, author, tags, initial_date, update_date)

# 输出到文件或直接打印出来
output_file = title + ".md"
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown模板已成功写入 {output_file}")