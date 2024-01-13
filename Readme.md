# Bot de Discord para la Gestión de Tareas

Este es un bot de Discord que permite a los usuarios gestionar sus tareas de manera eficiente.

## Características

- Añadir nuevas tareas para cualquier día de la semana con el comando `!Nuevatarea`.
- Ver las tareas del día actual o de un día específico con el comando `!tareas`.
- Ver todas las tareas de la semana con el comando `!Listatareas`.
- Los comandos no distinguen entre mayúsculas y minúsculas.
- Las tareas se guardan en un archivo JSON, por lo que persisten entre diferentes ejecuciones del bot.

## Comandos

- `!Nuevatarea <tarea> <dia>`: Añade una nueva tarea para el día especificado.
- `!tareas <dia>`: Muestra las tareas para el día especificado. Si no se especifica ningún día, muestra las tareas para el día actual.
- `!Listatareas`: Muestra todas las tareas de la semana.

## Uso

1. Clona este repositorio en tu máquina local.
2. Instala la biblioteca discord.py con pip: `pip install discord.py`.
3. Crea un bot en el portal de desarrolladores de Discord y obtén el token del bot.
4. Reemplaza `''` en el código con el token de tu bot.
5. Ejecuta el bot con Python 3: `python BotBuuk.py`.
6. Invita al bot a tu servidor de Discord e interactúa con él utilizando los comandos.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un problema o una solicitud de extracción para cualquier bug o mejora que desees añadir.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
