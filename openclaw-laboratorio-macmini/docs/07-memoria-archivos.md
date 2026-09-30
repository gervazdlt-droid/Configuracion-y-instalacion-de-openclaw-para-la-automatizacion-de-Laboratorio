# 7. Memoria y archivos

## Workspace

Usa carpetas separadas:

- `inbox/`: entradas sin revisar.
- `projects/`: proyectos activos.
- `results/`: resultados derivados y reportes.
- `archive/`: material cerrado.

Los datos originales deben estar fuera del workspace de escritura o montados en solo lectura.

## Archivos estructurados

`python/create_research_file.py` crea un registro Markdown con metadatos, hipótesis, archivos de entrada, modelo usado y revisión humana.

```bash
python python/create_research_file.py --title "Calibración HPGe maíz" --project espectrometria
```

## Memoria semántica

Para buscar en muchos documentos puede usarse `nomic-embed-text` y una base local. Antes de indexar, elimina credenciales, datos personales y archivos que no deban entrar en contexto. Conserva un inventario de qué carpetas fueron indexadas.
