#!/usr/bin/env bash
set -euo pipefail
models=("llama3.2:3b" "qwen2.5:7b" "qwen2.5-coder:7b" "nomic-embed-text")
for model in "${models[@]}"; do
  ollama pull "$model"
done
ollama list
