# 9. Gemini y selección de modelos

## Instalar el proveedor

La forma exacta depende de los plugins/proveedores que soporte la versión instalada de OpenClaw. Durante `openclaw onboard`, selecciona Gemini si aparece y proporciona la clave mediante un gestor de secretos.

Obtén la API key desde Google AI Studio y sigue sus condiciones de uso. Nunca la pegues en `openclaw-lab.example.json` ni en Discord.

## Política de selección

| Situación | Modelo preferido | Motivo |
|---|---|---|
| Datos sensibles o trabajo sin Internet | Ollama local | Privacidad y control |
| Clasificación y resúmenes cortos | modelo local rápido | Menor latencia |
| Python y shell | modelo local de código | Especialización |
| Documento grande o multimodal autorizado | Gemini | Contexto/capacidades |
| Decisión científica | modelo + revisión humana | El agente no sustituye al investigador |

## Fallback

Usa `config/model-routing.example.yaml` como política legible. Un fallback no debe enviar automáticamente datos restringidos a la nube: primero clasifica la sensibilidad y solicita autorización.

## Inventario de IAs instaladas

Documenta en cada equipo:

```bash
ollama list
openclaw --version
python3 --version
```

Registra nombre, versión, cuantización, memoria usada, velocidad aproximada y tareas en las que fue evaluado. Así se puede elegir entre las IAs locales, Gemini y otros proveedores de forma consciente.
