import sys
import importlib.util

def check(name):
    found = importlib.util.find_spec(name) is not None
    return f"{name}: {found}"

results = []
results.append(check("PIL")) # Pillow
results.append(check("cairosvg"))
results.append(check("svglib"))
results.append(check("selenium"))
results.append(check("pytesseract"))
results.append(check("easyocr"))
results.append(check("cv2")) # OpenCV

with open("env_capabilities.txt", "w") as f:
    f.write("\n".join(results))
