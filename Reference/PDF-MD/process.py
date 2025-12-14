"""
文献处理一体化脚本
功能：转录 PDF → 重命名为论文标题 → 更新索引

使用方法：
1. 将 PDF 放入 pdfs/ 目录
2. 运行 python process.py
3. 自动完成：转录 → 重命名 → 加入索引
"""
import os
import time
import requests
from pathlib import Path
from datetime import datetime

# PDF 页数检测
try:
    import pypdf
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

# 自动加载 .env 文件
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent.parent / ".env")
except ImportError:
    pass  # 如果没安装 dotenv，跳过（依赖手动设置环境变量）

# ============================================================
# 配置
# ============================================================
API_KEY = os.getenv("DATALAB_API_KEY")
API_URL = "https://www.datalab.to/api/v1/marker"

if not API_KEY:
    print("❌ 错误: 未设置 DATALAB_API_KEY 环境变量")
    print("请设置环境变量后再运行:")
    print("  Windows: set DATALAB_API_KEY=your_api_key")
    print("  或在 .env 文件中设置: DATALAB_API_KEY=your_api_key")
    exit(1)

# 目录（相对于脚本位置）
SCRIPT_DIR = Path(__file__).parent
PDF_DIR = SCRIPT_DIR / "pdfs"
OUTPUT_DIR = SCRIPT_DIR / "output_api"
DONE_DIR = SCRIPT_DIR / "pdfs_done"
INDEX_FILE = SCRIPT_DIR.parent / "_INDEX.md"
MAX_PAGES = 50  # 超过此页数需要确认

# 确保目录存在
PDF_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
DONE_DIR.mkdir(exist_ok=True)


def get_pdf_pages(pdf_path: Path) -> int:
    """获取 PDF 页数"""
    if not HAS_PYPDF:
        return -1
    try:
        with open(pdf_path, "rb") as f:
            reader = pypdf.PdfReader(f)
            return len(reader.pages)
    except:
        return -1


# ============================================================
# 步骤 1: PDF 转 Markdown
# ============================================================
def convert_pdf(pdf_path: Path, max_retries=3) -> dict:
    """调用 Marker API 转换单个 PDF"""
    headers = {"X-Api-Key": API_KEY}
    
    for attempt in range(max_retries):
        try:
            with open(pdf_path, "rb") as f:
                files = {"file": (pdf_path.name, f, "application/pdf")}
                response = requests.post(API_URL, files=files, headers=headers, timeout=60)
            
            if response.status_code != 200:
                print(f"    提交失败: {response.status_code}")
                continue
            
            data = response.json()
            if "request_check_url" not in data:
                print(f"    响应异常")
                continue
            
            check_url = data["request_check_url"]
            
            # 轮询等待完成
            for i in range(60):
                time.sleep(2)
                response = requests.get(check_url, headers=headers, timeout=30)
                data = response.json()
                
                if data.get("status") == "complete":
                    return data
                elif data.get("status") == "error":
                    print(f"    API 错误: {data.get('error', 'unknown')}")
                    break
        
        except requests.exceptions.RequestException as e:
            print(f"    网络错误 (尝试 {attempt+1}/{max_retries})")
            time.sleep(3)
    
    return None


# ============================================================
# 步骤 2: 提取论文标题并重命名
# ============================================================
def extract_title(md_path: Path) -> str:
    """从 MD 文件提取论文标题"""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read(5000)
    except:
        return None
    
    for line in content.split('\n'):
        line = line.strip()
        if not line or line.startswith('!') or line.startswith('See discussions'):
            continue
        if line.startswith('# '):
            title = line[2:].strip()
            return title.replace('"', "'")
    return None


def sanitize_filename(title: str) -> str:
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


def rename_md_file(md_path: Path) -> tuple:
    """重命名 MD 文件为论文标题，返回 (新路径, 标题)"""
    title = extract_title(md_path)
    if not title:
        return md_path, None
    
    new_name = sanitize_filename(title) + ".md"
    new_path = md_path.parent / new_name
    
    if md_path.name != new_name and not new_path.exists():
        try:
            md_path.rename(new_path)
            return new_path, title
        except:
            return md_path, title
    
    return md_path, title


# ============================================================
# 步骤 3: 更新索引
# ============================================================
def append_to_index(title: str, filename: str):
    """将新文献添加到索引"""
    if not INDEX_FILE.exists():
        return
    
    # 读取当前索引内容
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 检查是否已存在
    if filename in content:
        return
    
    # 计算新编号
    import re
    numbers = re.findall(r'\| (\d+) \|', content)
    next_num = max([int(n) for n in numbers], default=0) + 1
    
    # 构造新条目
    title_short = title[:50] + "..." if len(title) > 50 else title
    new_entry = f"| {next_num:02d} | {title_short} | `{filename}` |\n"
    
    # 在最后一个表格条目后添加
    # 找到 "## 使用说明" 之前插入
    if "## 使用说明" in content:
        content = content.replace("## 使用说明", new_entry + "\n## 使用说明")
    else:
        content += "\n" + new_entry
    
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"    已添加到索引: #{next_num:02d}")


# ============================================================
# 主流程
# ============================================================
def process_single_pdf(pdf_path: Path, skip_large: bool = False) -> str:
    """处理单个 PDF：转录 → 重命名 → 加入索引
    返回: 'success' | 'failed' | 'skipped'
    """
    print(f"\n📄 {pdf_path.name}")
    
    # 检查是否已处理过（output_api 中已有同名 MD）
    existing_md = OUTPUT_DIR / (pdf_path.stem + ".md")
    if existing_md.exists():
        print(f"  ⏭️ 已存在，跳过")
        # 清理源文件
        done_path = DONE_DIR / pdf_path.name
        if done_path.exists():
            pdf_path.unlink()
        else:
            pdf_path.rename(done_path)
        return "skipped"
    
    # 检查页数
    pages = get_pdf_pages(pdf_path)
    if pages > 0:
        print(f"  页数: {pages}")
        if pages > MAX_PAGES:
            if skip_large:
                print(f"  ⚠️ 跳过: 超过 {MAX_PAGES} 页")
                return "skipped"
            else:
                confirm = input(f"  ⚠️ 此文件有 {pages} 页，是否处理? (y/N): ")
                if confirm.lower() != 'y':
                    print(f"  跳过")
                    return "skipped"
    
    # 步骤 1: 转录
    print("  [1/3] 转录中...")
    start = time.time()
    result = convert_pdf(pdf_path)
    elapsed = time.time() - start
    
    if not result or "markdown" not in result:
        print(f"  ✗ 转录失败")
        return "failed"
    
    # 保存 MD 文件（先用原始文件名）
    temp_md_path = OUTPUT_DIR / (pdf_path.stem + ".md")
    with open(temp_md_path, "w", encoding="utf-8") as f:
        f.write(result["markdown"])
    print(f"  ✓ 转录完成 ({elapsed:.1f}s)")
    
    # 步骤 2: 重命名
    print("  [2/3] 重命名...")
    new_md_path, title = rename_md_file(temp_md_path)
    if title:
        print(f"    → {new_md_path.name[:50]}...")
    else:
        print(f"    (保留原名)")
        title = pdf_path.stem
    
    # 步骤 3: 加入索引
    print("  [3/3] 更新索引...")
    append_to_index(title, new_md_path.name)
    
    # 移动原始 PDF 到已完成目录
    done_path = DONE_DIR / pdf_path.name
    if done_path.exists():
        # 已存在同名文件，删除源文件
        pdf_path.unlink()
    else:
        pdf_path.rename(done_path)
    
    print(f"  ✅ 处理完成!")
    return "success"


def main():
    print("=" * 60)
    print("  📚 文献处理一体化脚本")
    print("  转录 → 重命名 → 加入索引")
    print("=" * 60)
    print(f"\n监控目录: {PDF_DIR}")
    
    pdf_files = list(PDF_DIR.glob("*.pdf"))
    
    if not pdf_files:
        print("\n没有找到待处理的 PDF 文件")
        print(f"请将 PDF 放入: {PDF_DIR}")
        return
    
    print(f"\n发现 {len(pdf_files)} 个 PDF 文件")
    
    success = 0
    failed = 0
    skipped = 0
    
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}]", end="")
        result = process_single_pdf(pdf_path)
        if result == "success":
            success += 1
        elif result == "skipped":
            skipped += 1
        else:
            failed += 1
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print(f"处理完成! 成功: {success} | 失败: {failed} | 跳过: {skipped}")
    print(f"输出目录: {OUTPUT_DIR}")
    print(f"索引文件: {INDEX_FILE}")
    if skipped > 0:
        print(f"\n💡 跳过的大文件可手动处理，或修改 MAX_PAGES 设置")


if __name__ == "__main__":
    main()
