# 6. Abrir una plataforma web con Python

Este repositorio incluye `python/open_lab_platform.py` como ejemplo seguro de automatización. Está diseñado para abrir una URL y, opcionalmente, completar el usuario sin guardar la contraseña en el código.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r python/requirements.txt
```

## Credenciales

Usa macOS Keychain o variables de entorno locales:

```bash
export LAB_PLATFORM_URL="https://plataforma-autorizada.example/login"
export LAB_PLATFORM_USER="tu_usuario"
# La contraseña se solicita de forma interactiva; no se guarda en Git.
python python/open_lab_platform.py --interactive
```

El ejemplo usa Playwright y selectores genéricos que deben adaptarse a la plataforma autorizada. No intenta evadir CAPTCHA, MFA, controles de acceso ni restricciones del sitio.

## Buenas prácticas

- Usa una cuenta de servicio con permisos mínimos.
- Mantén MFA activado cuando la plataforma lo permita.
- Pide confirmación antes de presionar botones que envíen, borren o publiquen.
- No guardes capturas con datos sensibles en un repositorio público.
- Registra fecha, usuario, URL y resultado sin registrar la contraseña.
