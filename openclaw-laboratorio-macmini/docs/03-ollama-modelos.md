# 3. Ollama y modelos locales

## Instalar y probar

```bash
brew install ollama
brew services start ollama
ollama --version
curl http://127.0.0.1:11434/api/tags
```

Si el servicio no está activo, prueba temporalmente:

```bash
ollama serve
```

## Modelos sugeridos

```bash
ollama pull llama3.2:3b
ollama pull qwen2.5:7b
ollama pull qwen2.5-coder:7b
ollama pull nomic-embed-text
```

Selecciona el tamaño con base en la memoria unificada del Mac mini. Un modelo más grande no siempre es mejor si la velocidad y la estabilidad son importantes.

## Pruebas

```bash
ollama list
ollama run llama3.2:3b "Resume en cinco puntos la función de un detector HPGe."
ollama run qwen2.5-coder:7b "Escribe una función Python que lea un CSV y valide columnas."
```

## Privacidad

Por defecto, una llamada a `127.0.0.1:11434` permanece en el equipo. La aplicación que use Ollama puede enviar telemetría o datos a otros servicios; revisa sus políticas por separado.
