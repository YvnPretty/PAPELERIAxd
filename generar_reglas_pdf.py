#!/usr/bin/env python3
import subprocess, os, re

md_path = "/home/yvnsu/ppeleria/Reglas_de_Negocio.md"
html_path = "/home/yvnsu/ppeleria/Reglas_de_Negocio.html"
pdf_path = "/home/yvnsu/ppeleria/Reglas_de_Negocio.pdf"

with open(md_path, "r", encoding="utf-8") as f:
    md = f.read()

def md_to_html(text):
    lines = text.split("\n")
    html_lines = []
    in_list = False

    for line in lines:
        line = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" style="max-width:180px;margin:6px auto;display:block;">', line)
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
        line = re.sub(r'`(.+?)`', r'<code>\1</code>', line)

        if line.startswith("#### "):
            html_lines.append(f"<h4>{line[5:]}</h4>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.strip() == "---":
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("<hr>")
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
<title>Reglas de Negocio - Papelería</title>
<style>
  body {{
    font-family: Arial, sans-serif;
    font-size: 12pt;
    line-height: 1.8;
    color: #1a1a1a;
    margin: 50px 70px;
    max-width: 860px;
  }}
  h1 {{
    font-size: 17pt;
    color: #1a1a2e;
    border-bottom: 2px solid #1a1a2e;
    padding-bottom: 6px;
    margin-top: 30px;
  }}
  h2 {{
    font-size: 14pt;
    color: #0f3460;
    margin-top: 30px;
  }}
  h3 {{
    font-size: 12pt;
    color: #444;
    margin-top: 22px;
    font-style: italic;
  }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 28px 0; }}
  p {{ margin: 10px 0; text-align: justify; }}
  ul {{ margin-left: 22px; }}
  li {{ margin-bottom: 6px; }}
  a {{ color: #0055bb; }}
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
    generated = html_path.replace(".html", ".pdf")
    if generated != pdf_path and os.path.exists(generated):
        os.rename(generated, pdf_path)
    print(f"✅ PDF generado: {pdf_path}")
else:
    print("❌ Error:", result.stderr)
