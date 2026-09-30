# 2. Instalación del Mac mini

## Preparación

1. Actualiza macOS.
2. Activa FileVault y usa una cuenta de laboratorio sin permisos de administrador para la operación diaria.
3. Activa copias de seguridad cifradas.
4. Define una carpeta de trabajo, por ejemplo `~/LabAssistant/`.
5. Instala Xcode Command Line Tools:

```bash
xcode-select --install
```

## Homebrew

Instala Homebrew desde https://brew.sh. Después verifica:

```bash
brew update
brew doctor
brew install python node ollama
```

En Apple Silicon, Homebrew normalmente usa `/opt/homebrew`. Abre una terminal nueva si el instalador solicita agregar Homebrew al `PATH`.

## Directorios

```bash
mkdir -p ~/LabAssistant/{workspace,logs,backups}
mkdir -p ~/.openclaw/workspace
```

No ejecutes el agente con `sudo`. No abras puertos de administración hacia Internet sin una VPN o un control de acceso equivalente.
