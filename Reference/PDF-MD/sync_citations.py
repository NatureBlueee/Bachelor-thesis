"""
引用文献同步脚本
功能：根据论文 REFERENCES 部分，将文献在 Cited/ 和 Uncited/ 之间移动

使用方法：
1. 在合并PR后运行 python sync_citations.py
2. 脚本会自动解析 Draft.md 的引用，移动对应文献
"""
import re
from pathlib import Path

# 目录配置
SCRIPT_DIR = Path(__file__).parent
REFERENCE_DIR = SCRIPT_DIR.parent
CITED_DIR = REFERENCE_DIR / "Cited"
UNCITED_DIR = REFERENCE_DIR / "Uncited"
DRAFT_FILE = REFERENCE_DIR.parent / "Target" / "Draft.md"

# 确保目录存在
CITED_DIR.mkdir(exist_ok=True)
UNCITED_DIR.mkdir(exist_ok=True)

# 手动映射：难以自动匹配的文献
MANUAL_MAPPINGS = {
    # "作者姓氏_年份": "文件名（不含.md）"
    "Bandura_1997": None,  # 经典著作，可能没有PDF
    "Braun_2006": "Using thematic analysis in psychology",
    "Cassell_2004": None,  # 经典著作
    "Cetindamar_2022": "Explicating AI Literacy of Employees at Digital Workplaces",
    "Creswell_2018": None,  # 经典著作
    "DeRue_2010": None,  # 需要查找
    "Detert_2007": "Leadership Behavior and Employee Voice - Is The Door Really Open",
    "French_1959": None,  # 经典著作
    "Guest_2020": "A simple method to assess and report thematic saturation in qualitative research",
    "Hennink_2021": "1-s2.0-S0277953621008558-main",
    "Hofstede_2001": None,  # 经典著作
    "Kamasak_2017": "Chapter 2Qualitative Methods in Organizational Research - An Example of Grounded Theory Data Analysi",
    "Kama_2017": "Chapter 2Qualitative Methods in Organizational Research - An Example of Grounded Theory Data Analysi",
    "Kipnis_1980": "Intraorganizational influence tactics - Explorations in getting one's way",
    "Kvale_2009": None,  # 经典著作
    "Long_2020": "Conceptualizing AI literacy - An exploratory review",
    "Malterud_2016": "Sample Size in Qualitative Interview Studies - Guided by Information Power",
    "Naeem_2023": "A Step-by-Step Process of Thematic Analysis to Develop a Conceptual Model in Qualitative Research",
    "Ng_2023": "Design and validation of the AI literacy questionnaire - The affective, behavioural, cognitive and e",
    "Pfeffer_1978": None,  # 经典著作
    "Prensky_2001": "Digital Natives, Digital Immigrants",
    "Roberts_2019": "Attempting rigour and replicability in thematic analysis of qualitative research data; a case study",
    "Saunders_2016": None,  # 需要查找
    "Schroth_2019": None,  # 需要查找
    "Scott_1994": "DETERMINANTS OF INNOVATIVE BEHAVIOR - A PATH MODEL OF INDIVIDUAL INNOVATION IN THE WORKPLACE",
    "Seemiller_2016": None,  # 经典著作
    "Tripathi_2021": "Reverse the Lens, Set Focus on the Followers - A Theoretical Framework of Resource Dependence, Upwar",
    "Wang_2022": "Measuring user competence in using artificial intelligence - validity and reliability of artificial",
    "Watkins_2025": "Zooming in on Generational Differences - Exploring Intergenerational Employee Relationships and the",
    "钟柏昌_2024": "何谓人工智能素养 -本质、构成与评价体系-",
}


def extract_citations_from_draft() -> list[dict]:
    """
    从论文初稿中提取所有引用
    返回: [{"author": "Bandura", "year": "1997", "key": "Bandura_1997"}, ...]
    """
    if not DRAFT_FILE.exists():
        print(f"❌ 找不到论文文件: {DRAFT_FILE}")
        return []
    
    with open(DRAFT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 找到 REFERENCES 部分
    ref_match = re.search(r'(?:^|\n)REFERENCES\s*\n(.*?)(?:\n(?:APPENDIX|附录)|$)', 
                          content, re.DOTALL | re.IGNORECASE)
    if not ref_match:
        print("❌ 找不到 REFERENCES 部分")
        return []
    
    ref_section = ref_match.group(1)
    citations = []
    
    # 解析每个引用条目
    for line in ref_section.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('|'):
            continue
        
        # 英文格式: Author, A. B. (2020) 或 Author, A., & Co-author, B. (2020)
        eng_match = re.match(r'^([A-Z][a-zA-Z\-\']+)', line)
        year_match = re.search(r'\((\d{4})\)', line)
        
        # 中文格式: 作者, 作者. (2020)
        chn_match = re.match(r'^([\u4e00-\u9fff]+)', line)
        
        if year_match:
            year = year_match.group(1)
            if eng_match:
                author = eng_match.group(1)
                key = f"{author}_{year}"
                citations.append({"author": author, "year": year, "key": key})
            elif chn_match:
                author = chn_match.group(1)
                key = f"{author}_{year}"
                citations.append({"author": author, "year": year, "key": key})
    
    return citations


def find_file_by_name(filename_prefix: str, search_dirs: list[Path]) -> Path | None:
    """在目录中查找以指定前缀开头的文件"""
    for dir_path in search_dirs:
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("*.md"):
            if md_file.stem.startswith(filename_prefix) or filename_prefix in md_file.stem:
                return md_file
    return None


def sync_citations():
    """主同步函数"""
    print("=" * 60)
    print("  📚 引用文献同步")
    print("=" * 60)
    
    # 1. 提取引用
    print("\n[1/3] 解析论文引用...")
    citations = extract_citations_from_draft()
    print(f"    发现 {len(citations)} 条引用")
    
    if not citations:
        return
    
    # 2. 匹配并移动
    print("\n[2/3] 匹配文献文件...")
    all_dirs = [CITED_DIR, UNCITED_DIR]
    cited_files = set()
    matched = 0
    unmatched = []
    
    for cit in citations:
        key = cit["key"]
        mapped_name = MANUAL_MAPPINGS.get(key)
        
        md_file = None
        if mapped_name:
            md_file = find_file_by_name(mapped_name, all_dirs)
        
        if md_file:
            cited_files.add(md_file.name)
            matched += 1
            # 如果在 Uncited，移动到 Cited
            if md_file.parent == UNCITED_DIR:
                target = CITED_DIR / md_file.name
                if not target.exists():
                    md_file.rename(target)
                    print(f"    ✓ {cit['author']} ({cit['year']}) -> Cited/")
            else:
                print(f"    ○ {cit['author']} ({cit['year']}) 已在 Cited/")
        else:
            if mapped_name is None:
                # 经典著作，无PDF
                print(f"    - {cit['author']} ({cit['year']}) [经典著作/无PDF]")
            else:
                unmatched.append(cit)
    
    print(f"\n    匹配成功: {matched}/{len(citations)}")
    
    # 3. 将 Cited 中未引用的文件移回 Uncited
    print("\n[3/3] 清理未引用文献...")
    moved_back = 0
    for md_file in CITED_DIR.glob("*.md"):
        if md_file.name not in cited_files:
            target = UNCITED_DIR / md_file.name
            if not target.exists():
                md_file.rename(target)
                moved_back += 1
                print(f"    → {md_file.stem[:40]}... -> Uncited/")
    
    if moved_back > 0:
        print(f"    移回 Uncited: {moved_back} 个文件")
    else:
        print("    无需清理")
    
    # 4. 报告未匹配的引用
    if unmatched:
        print(f"\n⚠️ 未找到对应文件的引用 ({len(unmatched)}):")
        for cit in unmatched:
            print(f"    - {cit['author']} ({cit['year']})")
    
    print("\n" + "=" * 60)
    cited_count = len(list(CITED_DIR.glob('*.md')))
    uncited_count = len(list(UNCITED_DIR.glob('*.md')))
    print(f"同步完成! Cited: {cited_count} 篇 | Uncited: {uncited_count} 篇")


if __name__ == "__main__":
    sync_citations()
