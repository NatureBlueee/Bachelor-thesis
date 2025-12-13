"""
Marker API 批量转换脚本 (带重试)
"""
import os
import time
import requests
from pathlib import Path

# 自动加载 .env 文件
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent.parent / ".env")
except ImportError:
    pass

# API 配置
API_KEY = os.getenv("DATALAB_API_KEY")
API_URL = "https://www.datalab.to/api/v1/marker"

if not API_KEY:
    print("❌ 错误: 未设置 DATALAB_API_KEY 环境变量")
    print("请设置: set DATALAB_API_KEY=your_api_key")
    exit(1)

# 目录配置
PDF_DIR = Path("./pdfs")
OUTPUT_DIR = Path("./output_api")
DONE_DIR = Path("./pdfs_done")

OUTPUT_DIR.mkdir(exist_ok=True)
DONE_DIR.mkdir(exist_ok=True)

def convert_pdf(pdf_path: Path, max_retries=3) -> dict:
    """调用 Marker API 转换单个 PDF（带重试）"""
    headers = {"X-Api-Key": API_KEY}
    
    for attempt in range(max_retries):
        try:
            # 1. 提交文件
            with open(pdf_path, "rb") as f:
                files = {"file": (pdf_path.name, f, "application/pdf")}
                response = requests.post(API_URL, files=files, headers=headers, timeout=60)
            
            if response.status_code != 200:
                print(f"  提交失败: {response.status_code}")
                continue
            
            data = response.json()
            
            if "request_check_url" not in data:
                print(f"  响应异常")
                continue
            
            check_url = data["request_check_url"]
            
            # 2. 轮询等待完成
            for i in range(60):
                time.sleep(2)
                response = requests.get(check_url, headers=headers, timeout=30)
                data = response.json()
                
                if data.get("status") == "complete":
                    return data
                elif data.get("status") == "error":
                    print(f"  API 错误: {data.get('error', 'unknown')}")
                    break
            
        except requests.exceptions.RequestException as e:
            print(f"  网络错误 (尝试 {attempt+1}/{max_retries})")
            time.sleep(3)
            continue
    
    return None

def main():
    print("=" * 50)
    print("  Marker API 批量转换")
    print("=" * 50)
    
    pdf_files = list(PDF_DIR.glob("*.pdf"))
    
    if not pdf_files:
        print(f"没有找到 PDF 文件")
        return
    
    print(f"\n[发现] {len(pdf_files)} 个 PDF\n")
    
    success = 0
    failed = 0
    
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] {pdf_path.name}")
        
        start = time.time()
        result = convert_pdf(pdf_path)
        elapsed = time.time() - start
        
        if result and "markdown" in result:
            output_path = OUTPUT_DIR / (pdf_path.stem + ".md")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["markdown"])
            
            done_path = DONE_DIR / pdf_path.name
            if not done_path.exists():
                pdf_path.rename(done_path)
            
            print(f"  ✓ 完成 ({elapsed:.1f}s)")
            success += 1
        else:
            print(f"  ✗ 失败")
            failed += 1
        
        time.sleep(1)  # 避免太快
    
    print(f"\n完成! 成功: {success} | 失败: {failed}")
    print(f"输出: {OUTPUT_DIR.absolute()}")

if __name__ == "__main__":
    main()
