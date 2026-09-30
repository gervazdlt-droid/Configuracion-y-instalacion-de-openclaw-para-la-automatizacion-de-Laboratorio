# 10. Seguridad y credenciales

## Nunca hagas esto

- Subir `.env`, tokens, contraseñas, cookies o sesiones de navegador.
- Poner credenciales en prompts, issues o mensajes de Discord.
- Ejecutar código generado sin revisión.
- Dar al agente permisos de administrador.
- Exponer Ollama u OpenClaw a Internet sin autenticación y control de red.

## Checklist

```bash
chmod 700 ~/.openclaw
chmod 700 ~/LabAssistant
openclaw security audit --deep  # si la versión instalada lo soporta
```

Usa macOS Keychain (`security add-generic-password`) o el mecanismo de secretos documentado por la versión de OpenClaw. Revisa permisos con `ls -la` y rota tokens si aparecen en un log.

## Modelo de amenazas

Considera prompt injection en páginas web, archivos maliciosos, exfiltración por herramientas, abuso del bot de Discord y errores de identificación de archivos. La mitigación principal es la separación de permisos, confirmaciones humanas, allowlists y logs sin secretos.
