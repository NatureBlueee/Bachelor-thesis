"""
文献整理脚本 - 使用绝对路径
"""
import os
import re
from pathlib import Path

# 使用绝对路径
OUTPUT_DIR = Path(r"d:\Profolio\文章\Thesis\Graduate-thesis\Reference\PDF-MD\output_api")

def extract_title(file_path):
    """从MD文件中提取论文标题"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read(5000)
    except:
        return None
    
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line or line.startswith('!') or line.startswith('See discussions'):
            continue
        if line.startswith('# '):
            title = line[2:].strip()
            title = title.replace('"', "'")
            return title
    return None

def sanitize_filename(title):
    """清理标题使其成为有效文件名"""
    replacements = {
        ':': ' -',
        '/': '-',
        '\\': '-',
        '?': '',
        '*': '',
        '<': '',
        '>': '',
        '|': '-',
        '"': "'",
    }
    for old, new in replacements.items():
        title = title.replace(old, new)
    if len(title) > 100:
        title = title[:100]
    return title.strip()

def main():
    print(f"目录: {OUTPUT_DIR}")
    print(f"存在: {OUTPUT_DIR.exists()}")
    
    if not OUTPUT_DIR.exists():
        print("目录不存在!")
        return
    
    md_files = list(OUTPUT_DIR.glob("*.md"))
    print(f"找到 {len(md_files)} 个MD文件\n")
    
    results = []
    
    for i, md_file in enumerate(sorted(md_files), 1):
        old_name = md_file.name
        title = extract_title(md_file)
        
        if title:
            new_name = sanitize_filename(title) + ".md"
            new_path = md_file.parent / new_name
            
            action = "保持"
            if md_file.name != new_name:
                if new_path.exists():
                    action = "跳过(已存在)"
                else:
                    try:
                        md_file.rename(new_path)
                        action = "重命名"
                    except Exception as e:
                        action = f"错误:{e}"
                        new_name = old_name
            
            results.append({
                'num': i,
                'title': title[:60],
                'file': new_name,
                'action': action
            })
            print(f"[{i:02d}] {action}: {title[:50]}...")
        else:
            print(f"[{i:02d}] 无标题: {old_name[:40]}...")
    
    print(f"\n处理完成，共 {len(results)} 个文件")

if __name__ == "__main__":
    main()
