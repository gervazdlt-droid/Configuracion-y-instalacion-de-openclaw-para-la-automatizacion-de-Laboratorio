# 11. Operación y mantenimiento

## Health check

```bash
./scripts/health-check.sh
openclaw status
ollama list
```

## Actualizaciones

Haz backup de `~/.openclaw` antes de actualizar. Actualiza una dependencia a la vez, prueba con datos sintéticos y registra la versión.

## Respaldo

```bash
./scripts/backup-workspace.sh
```

No incluyas secretos en el backup. Cifra el dispositivo o el destino de respaldo.

## Pruebas de aceptación

- El agente responde por terminal.
- Puede crear un archivo dentro de `workspace/results`.
- No puede escribir en `workspace/archive` sin permiso explícito, si así se configuró.
- Un modelo local funciona sin Internet.
- Gemini funciona solo con datos autorizados.
- Discord responde únicamente en canales permitidos.
- La automatización web pide la contraseña de forma segura y no la registra.
