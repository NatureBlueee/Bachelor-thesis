import gzip
import shutil
import importlib.util
import os

def check_import(name):
    spec = importlib.util.find_spec(name)
    found = spec is not None
    print(f"{name}: {found}")
    return found

try:
    print("Decompressing...")
    # Using absolute paths to be safe, though CWD should be correct
    base_dir = r"d:\Profolio\文章\Thesis\Graduate-thesis\Reference\non-acadamic"
    input_path = os.path.join(base_dir, "Superagency_Ex4.svgz")
    output_path = os.path.join(base_dir, "Superagency_Ex4_debug.svg")
    
    with gzip.open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Decompressed to {output_path}")
except Exception as e:
    print(f"Error decompressing: {e}")

print("Checking libraries...")
has_pil = check_import("PIL")
has_pytesseract = check_import("pytesseract")
has_easyocr = check_import("easyocr")
has_cairosvg = check_import("cairosvg")
