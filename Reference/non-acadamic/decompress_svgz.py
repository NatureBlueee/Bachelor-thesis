import gzip
import shutil
from pathlib import Path
import os
import sys

# 设置标准输出编码为utf-8，防止中文路径打印报错
sys.stdout.reconfigure(encoding='utf-8')

directory = Path(r"d:\Profolio\文章\Thesis\Graduate-thesis\Reference\non-acadamic")

def decompress_svgz(file_path):
    output_path = file_path.with_suffix('.svg')
    try:
        if not file_path.exists():
            print(f"File not found: {file_path}")
            return
            
        with gzip.open(file_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Decompressed: {file_path.name} -> {output_path.name}")
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")

if __name__ == "__main__":
    print(f"Searching in: {directory}")
    try:
        svgz_files = list(directory.glob("*.svgz"))
        print(f"Found {len(svgz_files)} svgz files.")
        for file in svgz_files:
            decompress_svgz(file)
    except Exception as e:
        print(f"Global error: {e}")
