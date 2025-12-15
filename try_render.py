import importlib.util
try:
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPM
    print("svglib and reportlab imported.")
    
    is_pil = importlib.util.find_spec("PIL") is not None
    print(f"PIL available: {is_pil}")
    
    if is_pil:
        import os
        base = r"d:\Profolio\文章\Thesis\Graduate-thesis\Reference\non-acadamic"
        svg_path = os.path.join(base, "Superagency_Ex4_debug.svg")
        png_path = os.path.join(base, "Superagency_Ex4_preview.png")
        
        drawing = svg2rlg(svg_path)
        renderPM.drawToFile(drawing, png_path, fmt="PNG")
        print(f"Rendered PNG to {png_path}")
except Exception as e:
    print(f"Error: {e}")
