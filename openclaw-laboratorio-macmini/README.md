# OpenClaw Lab Assistant para Mac mini

Guía reproducible para instalar y operar **OpenClaw** en un Mac mini como asistente de un laboratorio de investigación, combinando modelos locales mediante **Ollama** con modelos en la nube como **Gemini** y otros proveedores compatibles.

> **Estado del proyecto:** plantilla educativa y operativa. Las pantallas, nombres de opciones y comandos de OpenClaw pueden cambiar entre versiones. Antes de ejecutar comandos en producción, confirma la sintaxis en la documentación oficial.

## Objetivos

- Instalar las herramientas base en macOS Apple Silicon.
- Ejecutar varias IAs locales con Ollama.
- Conectar OpenClaw con modelos locales y servicios externos.
- Elegir el modelo adecuado según la tarea: privacidad, razonamiento, código, velocidad o contexto.
- Definir un asistente para un laboratorio de investigación.
- Automatizar tareas controladas: abrir una plataforma web, crear archivos, organizar resultados y preparar reportes.
- Conectar el agente a Discord con permisos mínimos.
- Mantener credenciales fuera del repositorio y aplicar controles de seguridad.

## Índice

1. [Arquitectura](docs/01-arquitectura.md)
2. [Instalación del Mac mini](docs/02-instalacion-macos.md)
3. [Ollama y modelos locales](docs/03-ollama-modelos.md)
4. [OpenClaw y onboarding](docs/04-openclaw.md)
5. [Configuración del asistente de laboratorio](docs/05-asistente-laboratorio.md)
6. [Automatización web con Python](docs/06-automatizacion-web.md)
7. [Archivos, memoria y workspace](docs/07-memoria-archivos.md)
8. [Discord](docs/08-discord.md)
9. [Gemini y selección de modelos](docs/09-gemini-y-model-routing.md)
10. [Seguridad y credenciales](docs/10-seguridad.md)
11. [Operación, pruebas y mantenimiento](docs/11-operacion.md)
12. [Solución de problemas](docs/12-troubleshooting.md)
13. [Caso de despliegue en laboratorio](docs/13-caso-despliegue-produccion.md)

## Inicio rápido

```bash
# 1. Instalar Homebrew si aún no existe; después:
brew install python node ollama
brew services start ollama

# 2. Descargar modelos según la memoria unificada disponible
ollama pull qwen2.5:7b
ollama pull llama3.2:3b
ollama pull nomic-embed-text

# 3. Instalar OpenClaw usando la ruta oficial vigente
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon

# 4. Verificar
ollama list
openclaw --version
openclaw status
```

Para una instalación segura, lee los documentos en orden y no pegues tokens reales en archivos del repositorio.

## Selección de modelos

El proyecto contempla un conjunto mixto:

| Tipo | Ejemplo | Uso recomendado |
|---|---|---|
| Local rápido | `llama3.2:3b` | clasificación, borradores, tareas rutinarias |
| Local de código | `qwen2.5-coder:7b` | Python, shell y transformación de datos |
| Local general | `qwen2.5:7b` | asistente de laboratorio y análisis textual |
| Embeddings | `nomic-embed-text` | búsqueda semántica en documentos locales |
| Nube | Gemini | contexto amplio, tareas complejas y multimodales |

Los nombres concretos dependen de la memoria del Mac mini y de los modelos disponibles. No es necesario instalar todos: empieza por uno general, uno de código y embeddings.

## Reglas para un laboratorio

- El agente **no debe inventar resultados científicos**.
- Toda acción que modifique datos originales, publique resultados, envíe mensajes externos o use credenciales debe requerir confirmación.
- Los datos originales se conservan en modo solo lectura.
- Los resultados derivados deben incluir fecha, modelo, versión del código y parámetros.
- Las credenciales se guardan en macOS Keychain, variables de entorno locales o el gestor de secretos de OpenClaw; nunca en Git.
- Discord se usa como interfaz, no como almacén de datos sensibles.

## Estructura

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docs/
├── config/
│   ├── openclaw-lab.example.json
│   └── model-routing.example.yaml
├── security/
│   ├── SECURITY.md
│   └── checklist.md
├── scripts/
│   ├── bootstrap-mac.sh
│   ├── install-models.sh
│   ├── health-check.sh
│   └── backup-workspace.sh
├── python/
│   ├── requirements.txt
│   ├── open_lab_platform.py
│   └── create_research_file.py
├── workspace/
│   ├── projects/.gitkeep
│   ├── results/.gitkeep
│   ├── inbox/.gitkeep
│   └── archive/.gitkeep
└── examples/
    └── tarea-laboratorio.md
```

## Experiencia de despliegue y colaboración

### Despliegue y configuración de agente de IA para automatización de laboratorio

**Colaboración con investigador · Agente open-source desplegado en producción**

Este proyecto documenta la colaboración con un investigador para desplegar y adaptar un agente de IA de código abierto a un entorno real de laboratorio. El agente fue instalado en una **Mac mini utilizada como servidor del laboratorio** y continúa desplegado en uso activo.

El trabajo incluyó:

- Instalación y configuración de **OpenClaw** en la Mac mini, con un workspace dedicado y controles de operación.
- Implementación de una interfaz de operación remota mediante **Discord**, para que el investigador pudiera enviar instrucciones al agente desde un chat autorizado.
- Configuración de **APIs, credenciales y acceso controlado a archivos**, permitiendo trabajar con los archivos CSV utilizados como bases de datos del laboratorio.
- Implementación de selección entre distintos modelos de IA, evitando que el sistema quedara ligado a un único LLM.
- Adaptación del agente a un caso de uso real como asistente de investigación: automatización de tareas, generación de archivos, organización de resultados y gestión de datos.

### Herramientas utilizadas

`OpenClaw` · `Discord API` · `Python` · `Ollama` · `Gemini` · `APIs de modelos de IA (LLMs)` · `macOS`

La configuración mantiene separación entre datos originales, resultados derivados y secretos. Las acciones externas o destructivas requieren revisión o confirmación humana.

## Fuentes oficiales

- OpenClaw: https://github.com/openclaw/openclaw
- Sitio de instalación: https://openclaw.ai
- Ollama: https://ollama.com
- Gemini API: https://ai.google.dev/gemini-api/docs
- Discord Developer Portal: https://discord.com/developers/applications

## Licencia

MIT para los archivos de esta plantilla. Las marcas, modelos y servicios externos conservan sus propias licencias y condiciones.
