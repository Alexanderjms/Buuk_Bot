import discord
from discord.ext import commands
import datetime
import json

# Cargar las tareas desde un archivo al iniciar el bot (De forma que siempre que se inicie el bot las tareas queden guardadas). 
with open('tareas.json', 'r', encoding='utf-8') as f:
    lista_de_tareas = json.load(f)

try:
    with open('tareas.json', 'r', encoding='utf-8') as f:
        lista_de_tareas = json.load(f)
except FileNotFoundError:

    # Si el archivo no existe, usar una lista de tareas vacía
    lista_de_tareas = {
        "Lunes": [],
        "Martes": [],
        "Miércoles": [],
        "Jueves": [],
        "Viernes": [],
        "Sábado": [],
        "Domingo": []
    }

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print('En línea')
    canal = bot.get_channel() # Dentro del paréntesis colocar la ID de tu canal de tu servidor. 

    await canal.send('¡Hola! Soy Buuk')

@bot.command()
async def tareas(ctx, dia=None):
    dias_en_español = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    if dia is None:
        dia_actual = datetime.datetime.today().strftime('%A')
        dia_actual_español = dias_en_español[dia_actual]
    else:
        dia_actual_español = dia.capitalize()
    if dia_actual_español in lista_de_tareas:
        mensaje = "Tareas para " + ("hoy (" + dia_actual_español + "):\n" if dia is None else "el día " + dia_actual_español + ":\n")
        for tarea in lista_de_tareas[dia_actual_español]:
            mensaje += "- " + tarea + "\n"
        await ctx.send(mensaje)
    else:
        await ctx.send("No hay tareas para hoy." if dia is None else f'"{dia}" no es un día válido. Por favor, introduce un día de la semana en español.')

@bot.command()
async def Nuevatarea(ctx, *args):
    dia_sin_tilde = args[-1].lower()  # Convertir a minúsculas
    tarea = ' '.join(args[:-1])  # Todos los demás argumentos son la tarea

    # Mapeo de días sin tildes a días con tildes
    dias_con_tilde = {
        "lunes": "Lunes",
        "martes": "Martes",
        "miercoles": "Miércoles",
        "jueves": "Jueves",
        "viernes": "Viernes",
        "sabado": "Sábado",
        "domingo": "Domingo"
    }

    # Obtener el día con tilde correspondiente al día sin tilde
    dia_con_tilde = dias_con_tilde.get(dia_sin_tilde)

    if dia_con_tilde and dia_con_tilde in lista_de_tareas:
        lista_de_tareas[dia_con_tilde].append(tarea)
        await ctx.send(f'La tarea "{tarea}" ha sido añadida para el día {dia_con_tilde}.')
        # Guardar las tareas en un archivo
        with open('tareas.json', 'w', encoding='utf-8') as f:
            json.dump(lista_de_tareas, f, ensure_ascii=False)
    else:
        await ctx.send(f'"{dia_sin_tilde}" no es un día válido. Por favor, introduce un día de la semana en español.')

@bot.command()
async def Listatareas(ctx):
    mensaje = "Tareas de la semana:\n\n"
    for dia, tareas in lista_de_tareas.items():
        mensaje += f"Tareas para el día {dia}:\n"
        for tarea in tareas:
            mensaje += f"- {tarea}\n"
        mensaje += "\n"
    await ctx.send(mensaje)

bot.run('') # Introduce aquí tu token
