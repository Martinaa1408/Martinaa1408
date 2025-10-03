import re

svg_path = "dist/fairy-contribution-graph.svg"

with open(svg_path, "r", encoding="utf-8") as f:
    svg_content = f.read()

# Trova tutti i <rect .../> del serpente
rect_pattern = re.compile(r"<rect([^>]*)/>")

matches = list(rect_pattern.finditer(svg_content))

# Se ci sono segmenti, prendi solo l'ultimo → la "testa" del serpente
if matches:
    last = matches[-1]
    attrs = last.group(1)

    x_match = re.search(r'x="([\d\.]+)"', attrs)
    y_match = re.search(r'y="([\d\.]+)"', attrs)

    if x_match and y_match:
        x = float(x_match.group(1)) + 2
        y = float(y_match.group(1)) + 6
        fairy = f'<text x="{x}" y="{y}" font-size="8">🧚</text>'

        # Rimuovi tutti i <rect>, poi inserisci solo la fatina
        svg_content = rect_pattern.sub("", svg_content)
        svg_content = svg_content.replace("</svg>", fairy + "\n</svg>")

# Salva il nuovo SVG
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print("✨ Fatina singola inserita con successo!")
