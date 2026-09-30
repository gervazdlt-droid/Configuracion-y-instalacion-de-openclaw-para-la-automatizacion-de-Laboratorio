import argparse, datetime
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--title', required=True)
p.add_argument('--project', required=True)
a = p.parse_args()
root = Path(__file__).resolve().parents[1] / 'workspace' / 'results'
root.mkdir(parents=True, exist_ok=True)
slug = ''.join(c.lower() if c.isalnum() else '-' for c in a.title).strip('-')
out = root / f"{datetime.date.today()}-{slug}.md"
out.write_text(f'''# {a.title}\n\n- Proyecto: {a.project}\n- Fecha: {datetime.datetime.now().isoformat(timespec="seconds")}\n- Estado: borrador\n- Modelo/agente: completar\n- Revisión humana: pendiente\n\n## Objetivo\n\nCompletar.\n\n## Archivos de entrada\n\nCompletar.\n\n## Método\n\nCompletar.\n\n## Resultados\n\nCompletar.\n\n## Limitaciones y revisión\n\nCompletar antes de compartir.\n''')
print(out)
