#!/usr/bin/env python3
import subprocess, os, re

md_path = "/home/yvnsu/ppeleria/Reporte_Final_Analisis.md"
html_path = "/home/yvnsu/ppeleria/Reporte_Final_Analisis.html"
pdf_path = "/home/yvnsu/ppeleria/Reporte_Final_Analisis.pdf"

with open(md_path, "r", encoding="utf-8") as f:
    md = f.read()

def md_to_html(text):
    lines = text.split("\n")
    html_lines = []
    in_list = False

    for line in lines:
        # Imágenes
        line = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" style="max-width:100%;margin:10px auto;display:block;">', line)
        # links
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
        # Negrita
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
        # Cursiva
        line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
        # código inline
        line = re.sub(r'`(.+?)`', r'<code>\1</code>', line)

        # Encabezados
        if line.startswith("#### "):
            html_lines.append(f"<h4>{line[5:]}</h4>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        # HR
        elif line.strip() == "---":
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("<hr>")
        # Listas
        elif line.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{line[2:]}</li>")
        elif line.strip().startswith(("<div", "</div")):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(line)
        elif line.strip() == "":
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{line}</p>")

    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)

body = md_to_html(md)

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Reporte Final - Papelería</title>
<style>
  body {{
    font-family: Arial, sans-serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #222;
    margin: 40px 60px;
    max-width: 900px;
  }}
  h1 {{ font-size: 18pt; color: #1a1a2e; border-bottom: 2px solid #1a1a2e; padding-bottom: 4px; }}
  h2 {{ font-size: 15pt; color: #16213e; margin-top: 28px; }}
  h3 {{ font-size: 13pt; color: #0f3460; }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 24px 0; }}
  ul {{ margin-left: 20px; }}
  li {{ margin-bottom: 6px; }}
  p {{ margin: 8px 0; text-align: justify; }}
  a {{ color: #0066cc; }}
  img {{ max-width: 100%; }}
  [align="center"] {{ text-align: center; }}
  strong {{ color: #111; }}
</style>
</head>
<body>
{body}
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML generado: {html_path}")

result = subprocess.run(
    ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir",
     "/home/yvnsu/ppeleria", html_path],
    capture_output=True, text=True
)
print(result.stdout)
if result.returncode == 0:
    # LibreOffice genera el PDF con el mismo nombre base del HTML
    generated = html_path.replace(".html", ".pdf")
    if generated != pdf_path and os.path.exists(generated):
        os.rename(generated, pdf_path)
    print(f"✅ PDF generado: {pdf_path}")
else:
    print("❌ Error:", result.stderr)
