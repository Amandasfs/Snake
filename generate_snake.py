# Importar as bibliotecas necessárias
import os
import json
import random
from datetime import datetime

# Configurações
WIDTH = 52
HEIGHT = 7
OUTPUT_FILE = 'snake.svg'

# Cores para a cobrinha
COLORS = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]

def generate_snake():
    # Gerar o corpo da cobrinha
    snake_body = []
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if random.random() < 0.1:
                snake_body.append((i, j))
    
    # Gerar o SVG
    svg_content = f'<svg viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">\n'
    for x, y in snake_body:
        color = random.choice(COLORS)
        svg_content += f'  <rect x="{x}" y="{y}" width="1" height="1" fill="{color}" />\n'
    svg_content += '</svg>'
    
    # Salvar o SVG em um arquivo
    with open(OUTPUT_FILE, 'w') as file:
        file.write(svg_content)
    
    print(f'Snake generated: {OUTPUT_FILE}')

if __name__ == "__main__":
    generate_snake()
