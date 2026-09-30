# 12. Solución de problemas

## `ollama: command not found`

Cierra y abre Terminal. Comprueba `which ollama`. Si usaste Homebrew en Apple Silicon, confirma que `/opt/homebrew/bin` esté en `PATH`.

## Modelo no encontrado

El nombre debe coincidir exactamente con `ollama list`. Vuelve a ejecutar `ollama pull NOMBRE:TAG`.

## OpenClaw no inicia

Ejecuta `openclaw --version`, `openclaw status` y revisa el log que indique tu versión. No borres `~/.openclaw` sin backup.

## Discord no responde

Revisa token, invitación, intents, permisos del canal, allowlist y si el bot requiere mención. Regenera el token si sospechas que fue expuesto.

## La automatización web falla

Los selectores HTML cambian. Usa la herramienta de inspección del navegador, adapta los selectores y prueba con una cuenta sin permisos destructivos. CAPTCHA y MFA deben resolverse manualmente.

## El modelo local es lento

Usa un modelo menor, reduce el contexto, cierra aplicaciones, revisa memoria unificada y evita ejecutar varios modelos pesados simultáneamente.
