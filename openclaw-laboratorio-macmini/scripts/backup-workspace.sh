#!/usr/bin/env bash
set -euo pipefail
src="${1:-$HOME/.openclaw}"
out="${2:-$HOME/LabAssistant/backups/openclaw-$(date +%Y%m%d-%H%M%S).tar.gz}"
mkdir -p "$(dirname "$out")"
tar --exclude='*.env' --exclude='*secret*' --exclude='*token*' -czf "$out" "$src"
echo "Backup creado: $out"
