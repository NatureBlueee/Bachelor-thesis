
import gzip
from pathlib import Path
import sys

# 设置标准输出编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')

file_path = Path(r"d:\Profolio\文章\Thesis\Graduate-thesis\Reference\non-acadamic\Superagency_Ex2.svgz")

try:
    if not file_path.exists():
        print(f"File not found: {file_path}")
    else:
        print(f"File size: {file_path.stat().st_size} bytes")
        with gzip.open(file_path, 'rt', encoding='utf-8') as f:
            content = f.read(200)
            print("--- Content Preview ---")
            print(content)
            print("--- End Preview ---")
except Exception as e:
    print(f"Error: {e}")
