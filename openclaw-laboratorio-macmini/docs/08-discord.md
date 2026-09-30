# 8. Discord

## Crear el bot

1. Entra a https://discord.com/developers/applications.
2. Crea una aplicación y un bot.
3. Copia el token una sola vez a un gestor de secretos.
4. Activa solo los intents necesarios.
5. Genera una invitación con `bot` y `applications.commands`.
6. Usa permisos mínimos: ver canales, enviar mensajes, leer historial y adjuntar archivos si es necesario.

No concedas `Administrator` salvo una prueba aislada y temporal.

## Diseño de canales

- `#lab-general`: consultas de bajo riesgo.
- `#lab-codigo`: scripts y revisión técnica.
- `#lab-resultados`: reportes no sensibles y aprobados.
- `#lab-alertas`: errores operativos.

Configura una lista de usuarios y canales permitidos. Requiere mención para evitar que el agente responda a todo el servidor.

## Seguridad

Discord no debe recibir contraseñas, claves API, datos personales innecesarios ni datos de investigación restringidos. Para una acción con efectos externos, responde con un resumen y exige confirmación explícita.

Consulta la sintaxis de integración de Discord de la versión instalada con `openclaw onboard` y la documentación oficial; la configuración de `config/openclaw-lab.example.json` es una plantilla, no un archivo listo para pegar sin revisión.
