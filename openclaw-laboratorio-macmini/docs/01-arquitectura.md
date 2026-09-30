# 1. Arquitectura

```text
Discord / Terminal / Web UI
          │
          ▼
       OpenClaw Gateway
          │
   ┌──────┼────────┐
   ▼      ▼        ▼
Ollama  Gemini  Herramientas
local   nube    Python/macOS
          │
          ▼
 ~/.openclaw/workspace
```

## Componentes

- **Mac mini:** equipo dedicado, idealmente con usuario separado para el agente.
- **OpenClaw:** orquestador del agente, canales, herramientas y workspace.
- **Ollama:** servidor local para inferencia sin enviar el contenido a un proveedor externo.
- **Gemini:** proveedor opcional para tareas que requieran sus capacidades y cuyo contenido esté autorizado para salir del equipo.
- **Python:** automatizaciones explícitas, reproducibles y revisables.
- **Discord:** interfaz de conversación; debe limitarse a canales y usuarios autorizados.

## Principio de mínimo privilegio

El agente recibe solo acceso a la carpeta del laboratorio que necesita. Primero se prueba en `workspace/` con datos ficticios; luego se amplían permisos. Las acciones destructivas o externas usan confirmación humana.
