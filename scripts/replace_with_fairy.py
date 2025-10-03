import re

svg_path = "dist/fairy-contribution-graph.svg"

with open(svg_path, "r", encoding="utf-8") as f:
    svg_content = f.read()


rect_pattern = re.compile(r"<rect([^>]*)/>")

def rect_to_fairy(match):
    attrs = match.group(1)
    x_match = re.search(r'x="([\d\.]+)"', attrs)
    y_match = re.search(r'y="([\d\.]+)"', attrs)
    if not x_match or not y_match:
        return match.group(0)
    x = float(x_match.group(1)) + 2
    y = float(y_match.group(1)) + 6
    return f'<text x="{x}" y="{y}" font-size="8">🧚</text>'

new_svg_content = rect_pattern.sub(rect_to_fairy, svg_content)

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(new_svg_content)

print("✨ Fatina inserita con successo!")
