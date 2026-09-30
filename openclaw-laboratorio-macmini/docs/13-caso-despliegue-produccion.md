# Caso de despliegue: agente de IA para automatización de laboratorio

## Resumen

Este caso describe la colaboración con un investigador para instalar, configurar y adaptar un agente de IA de código abierto a las operaciones de un laboratorio. El agente fue desplegado en una Mac mini utilizada como servidor del laboratorio y permanece en uso activo.

> La documentación de este caso no incluye credenciales, tokens, datos de investigación ni identificadores privados. Los nombres de rutas, modelos y canales deben sustituirse por los valores autorizados de cada instalación.

## Participación y contexto

**Rol:** colaboración técnica con investigador.

**Resultado:** agente open-source desplegado en producción para apoyar tareas de automatización, gestión de archivos y procesamiento de información del laboratorio.

## Trabajo realizado

### 1. Instalación y configuración en Mac mini

Se preparó la Mac mini como servidor del laboratorio, instalando y configurando OpenClaw, el entorno de Python, Ollama y las herramientas de operación. Se definió un workspace dedicado para separar:

- archivos recibidos;
- proyectos en proceso;
- resultados derivados;
- archivos archivados;
- logs y respaldos.

La instalación se realizó con criterios de operación continua: verificación de servicios, backups, permisos restringidos y recuperación ante fallos.

### 2. Interfaz remota mediante Discord

Se implementó una interfaz de operación remota con la Discord API. El investigador podía enviar instrucciones al agente desde un chat, sin conectarse directamente a la Mac mini para cada tarea.

La integración se organizó con:

- servidor y canales autorizados;
- lista de usuarios permitidos;
- permisos mínimos para el bot;
- requerimiento de mención para activar al agente;
- separación de canales para tareas generales, código, resultados y alertas.

Discord funciona como interfaz de operación, no como almacén de credenciales o datos sensibles.

### 3. APIs, credenciales y archivos CSV

Se configuraron APIs de modelos de IA, credenciales de servicios y acceso controlado al workspace. El agente puede trabajar con archivos CSV utilizados como bases de datos del laboratorio para tareas como:

- inspección de columnas y metadatos;
- validación de formatos;
- generación de resúmenes;
- creación de archivos derivados;
- organización de resultados;
- preparación de reportes para revisión.

Las contraseñas y tokens no se incluyen en código ni en el repositorio. Se utilizan variables locales, macOS Keychain o el mecanismo de secretos disponible en la instalación.

### 4. Selección entre varios modelos

El sistema no queda ligado a un único LLM. Se configuró una política de selección según el tipo de tarea:

| Necesidad | Estrategia |
|---|---|
| Datos sensibles o trabajo sin Internet | modelo local mediante Ollama |
| Código Python y transformación de CSV | modelo local especializado en código |
| Clasificación y tareas rápidas | modelo local ligero |
| Documentos extensos o tareas autorizadas | Gemini u otro proveedor externo |
| Embeddings y búsqueda local | modelo de embeddings en Ollama |

La selección considera privacidad, velocidad, costo, capacidad de razonamiento y tamaño del contexto. Los datos restringidos no deben pasar automáticamente a un proveedor externo como fallback.

### 5. Adaptación al caso de uso real

OpenClaw se adaptó para funcionar como asistente de un investigador. Entre las tareas soportadas se encuentran:

- recibir instrucciones desde Discord;
- abrir una plataforma web autorizada mediante un script Python;
- crear archivos en la memoria interna de la Mac mini;
- leer y organizar CSV del laboratorio;
- generar reportes y documentos de trabajo;
- clasificar solicitudes y elegir el modelo más adecuado;
- conservar los archivos originales sin modificarlos;
- dejar registro de modelo, fecha, entradas y revisión pendiente.

Las tareas de publicación, eliminación, envío externo o modificación de datos originales requieren confirmación humana.

## Operación en producción

El agente continúa desplegado y en uso activo. La operación incluye:

```bash
openclaw status
ollama list
./scripts/health-check.sh
./scripts/backup-workspace.sh
```

Cada cambio importante se prueba primero con datos sintéticos o una copia de trabajo. Se mantiene una copia de la configuración antes de actualizar OpenClaw o cambiar la política de modelos.

## Resultados de la colaboración

- Se convirtió una instalación local en una herramienta accesible remotamente.
- El investigador obtuvo una interfaz conversacional para solicitar tareas.
- Se redujo la dependencia de un solo modelo de IA.
- Se automatizaron tareas repetitivas de archivos y datos.
- Se preservó la separación entre originales, resultados y secretos.
- Se dejó una base documentada para ampliar el asistente sin perder control operativo.

## Herramientas

- **OpenClaw:** agente y orquestación.
- **Discord API:** interfaz remota.
- **Python:** automatización y procesamiento de archivos.
- **Ollama:** ejecución de modelos locales.
- **Gemini y APIs de LLMs:** proveedores adicionales seleccionables.
- **macOS / Mac mini:** servidor del laboratorio.
- **CSV:** formato de intercambio y bases de datos operativas del laboratorio.

## Consideraciones de seguridad

No se deben publicar en GitHub:

- tokens de Discord;
- API keys de Gemini u otros proveedores;
- contraseñas de plataformas;
- cookies o sesiones de navegador;
- CSV con información restringida;
- logs que contengan secretos.

La carpeta `security/` contiene el checklist general y la política de reporte de incidentes.
