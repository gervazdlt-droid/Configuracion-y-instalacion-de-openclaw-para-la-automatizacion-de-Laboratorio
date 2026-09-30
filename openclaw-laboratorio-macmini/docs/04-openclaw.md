# 4. OpenClaw

## Instalación

Consulta primero la documentación oficial y revisa el instalador. La ruta publicada para macOS es:

```bash
curl -fsSL https://openclaw.ai/install.sh -o /tmp/openclaw-install.sh
less /tmp/openclaw-install.sh
bash /tmp/openclaw-install.sh
```

Después verifica:

```bash
openclaw --version
openclaw onboard --install-daemon
openclaw status
```

El wizard puede solicitar workspace, proveedor de modelo, canales y servicio en segundo plano. Acepta solo las integraciones que realmente usarás.

## Configuración

Usa `config/openclaw-lab.example.json` como referencia conceptual. La configuración exacta puede variar por versión; no reemplaces automáticamente tu archivo real sin una copia de seguridad.

```bash
cp config/openclaw-lab.example.json /tmp/openclaw-lab-review.json
cp -R ~/.openclaw ~/.openclaw.backup.$(date +%Y%m%d-%H%M%S)
```

## Verificación mínima

- `openclaw status` muestra el gateway.
- Ollama responde en `127.0.0.1:11434`.
- El agente puede leer un archivo de prueba.
- El agente no puede leer una carpeta de secretos.
- Las tareas de escritura usan el workspace permitido.
