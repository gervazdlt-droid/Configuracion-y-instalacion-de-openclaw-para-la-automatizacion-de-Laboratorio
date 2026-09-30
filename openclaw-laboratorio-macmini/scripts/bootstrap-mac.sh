#!/usr/bin/env bash
set -euo pipefail
if ! command -v brew >/dev/null 2>&1; then
  echo "Instala Homebrew desde https://brew.sh y vuelve a ejecutar este script."
  exit 1
fi
brew update
brew install python node ollama
mkdir -p "$HOME/LabAssistant" "$HOME/.openclaw/workspace"
echo "Base instalada. Ejecuta: brew services start ollama"
echo "Después instala OpenClaw con el instalador oficial y ejecuta openclaw onboard --install-daemon"
