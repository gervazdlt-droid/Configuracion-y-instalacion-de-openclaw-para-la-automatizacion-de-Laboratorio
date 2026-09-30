#!/usr/bin/env bash
set -u
printf 'Ollama: '; command -v ollama || true
printf 'OpenClaw: '; command -v openclaw || true
printf 'Python: '; python3 --version 2>&1 || true
printf '\nOllama API:\n'; curl -fsS http://127.0.0.1:11434/api/tags || true
printf '\n\nOpenClaw status:\n'; openclaw status 2>&1 || true
