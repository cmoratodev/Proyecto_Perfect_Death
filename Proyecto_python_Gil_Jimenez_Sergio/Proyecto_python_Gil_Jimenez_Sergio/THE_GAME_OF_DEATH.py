# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import time
from colorama import *
import pygame

# Iniciamos colorama y pygame
init()
pygame.init()



# Definimos las variables y las iniciamos
puntos = 0
vidas = 3
escenarios = ["Patio de la Escuela Primaria", "Restaurante Raisins", "Casa de Cartman", "Terreno Baldío de los Chicos"]
escenario_actual = -1
while True:
    print("Esta es la modificación de Carlos, a ver ahora como sales del juego....")
    input("Presiona ENTER para continuar...")

os.system("cls")
# Introducción al juego
print(Fore.YELLOW + """
 _____                                                                                                               _____ 
( ___ )-------------------------------------------------------------------------------------------------------------( ___ )
 |   |                                                                                                               |   | 
 |   |      _______.  ______    __    __  .___________. __    __     .______      ___      .______       __  ___     |   | 
 |   |     /       | /  __  \  |  |  |  | |           ||  |  |  |    |   _  \    /   \     |   _  \     |  |/  /  _  |   | 
 |   |    |   (----`|  |  |  | |  |  |  | `---|  |----`|  |__|  |    |  |_)  |  /  ^  \    |  |_)  |    |  '  /  (_) |   | 
 |   |     \   \    |  |  |  | |  |  |  |     |  |     |   __   |    |   ___/  /  /_\  \   |      /     |    <       |   | 
 |   | .----)   |   |  `--'  | |  `--'  |     |  |     |  |  |  |    |  |     /  _____  \  |  |\  \----.|  .  \   _  |   | 
 |   | |_______/     \______/   \______/      |__|     |__|  |__|    | _|    /__/     \__\ | _| `._____||__|\__\ (_) |   | 
 |   |                                                                                                               |   | 
 |   | .___________. __    __   _______      _______      ___      .___  ___.  _______      ______    _______        |   | 
 |   | |           ||  |  |  | |   ____|    /  _____|    /   \     |   \/   | |   ____|    /  __  \  |   ____|       |   | 
 |   | `---|  |----`|  |__|  | |  |__      |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  | |  |__          |   | 
 |   |     |  |     |   __   | |   __|     |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  | |   __|         |   | 
 |   |     |  |     |  |  |  | |  |____    |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  | |  |            |   | 
 |   |     |__|     |__|  |__| |_______|    \______| /__/     \__\ |__|  |__| |_______|    \______/  |__|            |   | 
 |   |                                                                                                               |   | 
 |   |  _______   _______     ___   .___________. __    __                                                           |   | 
 |   | |       \ |   ____|   /   \  |           ||  |  |  |                                                          |   | 
 |   | |  .--.  ||  |__     /  ^  \ `---|  |----`|  |__|  |                                                          |   | 
 |   | |  |  |  ||   __|   /  /_\  \    |  |     |   __   |                                                          |   | 
 |   | |  '--'  ||  |____ /  _____  \   |  |     |  |  |  |                                                          |   | 
 |   | |_______/ |_______/__/     \__\  |__|     |__|  |__|                                                          |   | 
 |___|                                                                                                               |___| 
(_____)-------------------------------------------------------------------------------------------------------------(_____)
""")
pygame.mixer.music.load("musica proyecto/intro_south.mp3")
pygame.mixer.music.play()
input()
os.system("cls")
pygame.mixer.music.stop()
# pausamos justo despues de que el usuario pulse enter

print(Fore.WHITE + "El Consejo de South Park, formado por Cartman, Kyle, Stan y Kenny, te reta a demostrar cómo logras morir de las formas más creativas posibles.")
print(Fore.WHITE + "Tu misión: superar cada uno de los escenarios absurdos y lograr las muertes más épicas.")
print(Fore.LIGHTMAGENTA_EX + '''
     _.-(_)._     ."          ".      .--""--.          _.-(__)-._
   .'________'.   | .--------. |    .'        '.      .:-'`____`'-:.
  [____________] /` |________| `\  /   .'``'.   \    /_.-"`_  _`"-._|
  /  / .\/. \  \|  / / .\/. \ \  ||  .'/.\/.\ .  |  /`   / .\/. \   `|
  |  \__/\__/  |\_/  \__/\__/  \_/|  : |_/\_| ;  |  |    \__/\__/    |
  \            /  \            /   \ '.\    /.' / .-\                /-.
  /'._  --  _.'\  /'._  --  _.'\   /'. `'--'` .'\/   '._-.__--__.-_.'   |
 /_   `""""`   _\/_   `""""`   _\ /_  `-./\.-'  _\.    `""""""""`    .'`|
(__/    '|    \ _)_|           |_)_/            \__)|        '       |   |
  |_____'|_____|   \__________/   |              |;`_________'________`;-'
  '-----------'    '----------'   '--------------'`--------------------`
     S T A N          K Y L E        K E N N Y         C A R T M A N''')



input(Fore.GREEN + "Presiona ENTER para comenzar tu aventura...")

os.system("cls")
# Selección del escenario inicial
escenario_actual = 0
print(Fore.BLUE + f"Te encuentras en el escenario inicial: {escenarios[escenario_actual]}")
print(Fore.LIGHTGREEN_EX +  """⠀⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣤⣎⣀⣀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣄⣀⡀⠀⠀⢀⣀⣀⣈⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀
⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠿⠟⠻⠛⠻⠿⠿⠿⠿⢿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣠⢤⣧⣤⣤⣵⡶⣶⣾⣷⡿⣿⣟⡿⣿⢿⣟⡿⣿⣻⢿⡿⣿⣻⢿⣟⣿⡷⣶⣶⣦⣤⣤⣤⣤⣤⣤⣀⠀⠀⠀⢀⣤⣤⣤⣾⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣷⣿⣿⣷⣦⣿⣿⣿⣽⢿⡽⣿⡽⣯⣿⣽⣯⢿⣯⢿⣽⣯⡿⣯⣷⣟⡿⣞⣷⢯⣿⡽⣯⣟⣿⣻⣷⣶⣾⢿⣿⣻⣽⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢿⠛⢻⣿⣾⣿⣿⣿⣾⣯⡿⠿⠽⢿⣽⣷⣿⣷⣯⣷⣿⠿⢾⣿⡾⣷⣿⣷⡿⠾⠟⠛⠾⣿⠛⢟⣿⠾⠷⠿⢾⡷⣯⠿⢾⡛⣷⠟⠳⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⠸⣿⣿⢻⡿⠿⢿⡟⠛⡻⣦⢰⠿⢿⠿⢿⡉⠉⠉⢋⣻⠿⠿⠾⢿⡋⠙⠛⠛⣳⡶⡿⠿⢿⣿⣼⠛⠋⠛⣶⠶⠶⠾⢿⡏⠙⢾⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢈⣸⣿⠠⠄⠒⠠⡧⠀⠄⠘⣿⠀⡏⡆⢸⡇⠀⠀⢀⣯⠐⠂⠢⢘⡇⠀⠀⠀⣿⠀⠔⠆⠀⣿⠛⠀⠀⠂⣿⠀⠇⠒⢸⡇⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢘⢈⡿⠦⣤⢦⡼⠇⠀⠂⠀⠻⣤⡴⢦⡼⠏⠀⠐⠀⢻⣤⡴⣤⡼⠇⠀⠠⠀⠻⢦⣤⠶⡽⠏⠀⠀⠀⠀⠻⣤⢦⠧⡼⠃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⠈⡇⠀⠠⠀⢲⣄⣤⣔⣶⣤⣌⣤⣴⣶⣷⣦⣤⣼⣤⣤⣤⣵⣦⣶⣶⣦⣄⣤⣤⣤⣤⣤⣤⣄⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⠭⠰⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⡀⠀⠀⠀⡀⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠿⠿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀⢸⠌⠰⡇⠀⠀⠀⠸⠿⢿⠿⠿⠿⠿⠿⠿⠿⡿⢿⣿⣿⠿⠿⠿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠂⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣁⣀⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣼⢬⢸⣧⢀⡀⠐⣀⠀⠀⠀⠀⠂⢀⠀⠀⡀⠄⠠⣖⡓⣒⡀⠀⢘⣙⣧⠀⠀⠄⠐⠀⠀⢄⠠⠀⠀⠄⠀⠀⠂⠀⠀⠀⠂⠀⠂⠰⣏⢉⣉⣉⣉⣙⣻⣛⣛⣻⣻⣿⢿⣿⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠰⢸⡿⢋⡛⢛⢹⡇⠀⠁⠀⣿⠉⡛⡛⢻⡇⠀⠀⣻⣿⣿⣾⣷⣿⡇⠀⠂⠀⣾⠛⢻⡙⡙⡷⠀⠀⠐⠀⣾⢛⡛⣛⢻⡆⠐⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠠⢸⣯⠈⠄⠊⢨⡧⠀⠄⠀⣿⠀⠇⠍⢹⡇⠀⢀⣿⣿⣿⣿⣿⣿⡇⠠⠀⠀⣿⡀⠃⢂⢉⡷⠀⠀⠀⠀⣿⠈⡅⢉⢸⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣼⣟⣛⣋⣛⣛⣁⣠⣀⣀⣉⣻⣋⣙⣛⣁⣀⣀⣿⣿⣿⣿⣿⣿⣇⣀⣠⣤⣬⣽⣿⣿⣿⣃⣤⡤⠤⠤⠬⠿⠿⠿⠿⠵⠤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠋⢩⣷⣶⣷⣧⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⣽⡟⣩⠥⣍⠌⡏⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹
⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠉⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡯⡱⢰⠱⢌⡜⡰⢙⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⣤⣤⣤⣬⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⡤⣺⡿⢥⠱⠌⡥⠚⡤⢎⠱⠬⠢⢽⡦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣤⣀⣀⣀⣀⣀⣀⣤⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣬
⣩⣍⣭⣩⣍⣭⣩⣍⣩⣍⣩⣍⣩⣍⣥⣉⣦⣉⣦⣅⣎⣴⣡⣎⣩⣍⣭⣩⣍⣢⣩⣍⣒⣬⣘⣜⣤⣙⣔⣊⣍⣎⣱⣂⣴⣑⣢⣑⣢⣱⣌⣢⣑⣆⡲⣌⣲⣌⣦⣑⣎⣴⣁⣎⣴⣁⣞⣄⣣⣒⢦⣑⣂⣖⣐⣢⣒⣼
⣿⣯⣷⣿⣽⣯⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿⣾⣧⣿⣾⣷⣿⣾⣽⣯⣿⣽⣯⣿⣷⣿⣾⣷⣿⣾⣽⣾⣽⣷⣿⣾⣽⣷⣯⣷⣿⣾⣷⣿⣾⣽⣯⣷⣾⣧⣿⣾⣧⣿⣾⣷⣿⣮⣿⣵⣯⣿⣽⣿⣾⣽⣷⣿⣾""" )

print(Fore.RED + "Cartman observa desde una silla de juez mientras Kenny asiente con entusiasmo.")
print(Fore.RED + "Opciones disponibles:")
print(Fore.BLUE + "1. Beber del río del retrete (sí, en serio).")
print(Fore.BLUE + "2. Jugar con un detonador encontrado en el suelo.")
print(Fore.BLUE + "3. Correr hacia el autobús escolar a toda velocidad.")
print(Fore.BLUE + "4. Escalar el poste de la bandera hasta la cima.")



opcion_elegida = int(input())
#nos aseguramos de que la opcion elegida es valida
while opcion_elegida < 1 or opcion_elegida > 4:
    print(Fore.RED + Style.BRIGHT + "Opción no válida. Por favor, elige un número entre 1 y 4.")
    opcion_elegida = int(input())

# Evaluar la acción inicial
if opcion_elegida == 4:
    puntos += 10
    print(Fore.GREEN + "¡Has alcanzado la cima y te electrocutaste con una tormenta eléctrica épica! ¡El Consejo está impresionado!")
    pygame.mixer.music.load("musica proyecto/dumb_ways.mp3")
    pygame.mixer.music.play()
    input()
else:
    vidas -= 1
    if opcion_elegida == 1:
        print(Fore.BLUE + "Beber del río del retrete te provoca una diarrea interminable... pero sigues vivo.")
        pygame.mixer.music.load("musica proyecto/Alerta.mp3")
        pygame.mixer.music.play()
        input()
    elif opcion_elegida == 2:
        print(Fore.BLUE + "El detonador no hace nada o eso parece en principio... de pronto kenny empieza a emitir un pitido y explota.")
        print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⣴⢚⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⠤⠤⢀⣀⡀⠀⠀⠀⠀⠃⡴⣻⠋⡟⢠⡇⡾⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠊⢡⠀⠂⡄⠂⡄⠂⠉⠒⣤⠀⡆⣾⢱⠃⣼⣥⣾⣿⡟⢹⢫⣾⠛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢊⠐⣈⣴⠶⠛⠛⠛⢿⣶⣶⣈⠌⠳⣿⣿⡿⣿⣟⣻⢷⣮⠽⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⠀⣀⠀⠀⡸⢁⠂⣼⣿⡁⠄⡀⡐⠉⠈⠉⢾⢹⣧⡀⠹⡄⠉⠑⠺⠛⠉⠀⠴⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠃⡘⢷⣴⠃⡆⣾⢳⡏⠀⠀⠿⡇⠀⠀⠀⠈⢧⢻⣷⠀⢻⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡤⠤⠤⣭⣿⣿⡎⡱⣿⡹⡇⠀⠀⠀⠐⡀⠆⠀⠀⢸⣼⢿⠂⣽⣀⣴⢋⢦⢹⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣷⣴⣾⠏⢉⡽⡹⢧⠀⢿⣷⡹⣄⠀⠀⠀⡘⠐⠀⠐⣟⡞⡼⢁⡾⠀⢺⣜⡊⣾⡃⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣾⣿⢿⡾⣷⣶⣾⠁⠁⠸⡇⠈⣇⠹⣎⣷⡆⠈⠀⠀⢀⣾⠏⣰⠇⣾⢁⡾⠉⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠼⠿⠛⠛⠛⠛⠛⢋⡧⢴⠤⣀⣘⣦⡈⠳⢌⡉⠙⠛⠒⠛⣯⣤⠞⣡⠞⠁⡘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢺⡌⢧⠹⡌⣧⠠⠉⠓⠦⢭⣍⣛⣛⣩⡽⣼⠛⠥⠄⠡⢀⠈⢧⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠣⢳⣎⣽⠓⠛⠓⠻⡄⡀⠂⠄⠠⢀⠉⢷⡀⠌⡀⢂⡴⠞⠉⠉⢉⣾⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢱⡀⠡⢈⠐⢀⠂⢀⢳⣠⠖⠋⢀⠂⠌⡀⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠲⠆⠖⠒⠛⠉⡉⡤⠚⠉⠉⠓⠒⢼⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠘⢀⠃⠘⠠⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣦⣄⣌⣤⣡⣶⣾⣿⣤⣤⣤⣤⣤⣴⣶⣶⣶⣦⣦⣤⣤⣀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⢿⠿⠿⠿⠿⠿⠻⠛⠛⠛⠛⠉⠉⠉⠁⠉⠉⠀⠀""")
        pygame.mixer.music.load("musica proyecto/O Dios Mio Han Matado a Kenny Hijos De Puta (mp3cut.net).mp3")
        pygame.mixer.music.play()
        input()
    elif opcion_elegida == 3:
        print(Fore.BLUE + "El autobús se detiene justo a tiempo. La vida sigue... aburrida.")
        pygame.mixer.music.load("musica proyecto/Alerta.mp3")
        pygame.mixer.music.play()
        input()
        
# Actualizamos los escenarios restantes
escenarios[escenario_actual] = ""  # Marcamos este escenario como visitado

os.system("cls")
# Bucle principal para los siguientes escenarios
while vidas > 0 and any(escenarios):
    print(Fore.GREEN + "Escenarios restantes:")
    for idx, escenario in enumerate(escenarios):
        if escenario:
            print(Fore.BLUE + f"{idx + 1}. {escenario}")
    
    print(Fore.YELLOW + "Elige un escenario al que viajar:")
    opcion_escenario = int(input())
    
    # Validar que el escenario no haya sido visitado
    while opcion_escenario < 1 or opcion_escenario > len(escenarios) or not escenarios[opcion_escenario - 1]:
        print(Fore.RED + "Opción no válida o escenario ya visitado. Elige otro:")
        opcion_escenario = int(input())
    
    os.system("cls")
    escenario_actual = opcion_escenario - 1
    print(Fore.BLUE + f"Has elegido: {escenarios[escenario_actual]}")
    
    # Opciones para el nuevo escenario
    if escenario_actual == 1:  # Restaurante Raisins
        print(Fore.LIGHTBLUE_EX + """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⡛⠛⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⣿⣻⣟⣯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⠉⡄⢣⠘⢄⠣⠘⡄⢂⠍⠻⢿⣿⣿⣿⣿⣿⣿⠿⡿⢿⡿⢿⠷⣿⢿⣿⡿⢿⠿⣟⣻⣯⢿⣽⣿⣿⣿⡿⠟⡛⡉⢅⠂⢆⡈⠍⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⡟⠩⢔⠨⠟⣿⣿⣿⣿⣿⣿⢟⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣥⣆⠡⣊⣴⣵⣾⣿⣿⣷⠾⢶⡮⠅⠥⢹⠻⢿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣟⣯⣿⣽⣿⣿⡿⣶⣿⣿⣿⡛⣉⠐⢆⠓⠌⡰⢈⣼⣤⣆⠱⠠⢃⠨⠝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⢆⠱⠊⡜⡘⢠⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⢯⣿⣻⣿⢿⣻⣯⣟⣾⣽⣷⣀⣀⠀⠀⠀⠀⡀⢀⣄⡹⣦⣄⠀⠀⠀⠀⢤⣿⣿⣿⣿⣿⣿⣿⢿⣻⣽⣟⣿⣶⣿⣶⣾⣾⣿⡿⣟⡿⣿⣿⣶⣧⣶⣷⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣾⣿⣶⣶⣷⣦⣭⣂⣩⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣽⡾⣿⣽⣻⢷⣻⣾⣻⣽⡾⣽⣳⣿⣿⡄⣈⢳⡄⢠⢐⣿⡏⢩⣹⣻⡏⢷⢦⡀⣠⠼⢿⣿⣻⢯⣷⢿⣞⡿⣯⣷⢯⣷⣟⣾⣽⣳⡿⣾⡽⣟⣿⣳⣯⢿⣽⣻⢾⣳⡿⣯⣟⣿⣿⣿⣿⣿⣿
            ⣿⣿⣹⢿⣹⡿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⢿⣏⣿⣹⣷⣏⡿⣷⣏⡿⣿⣹⡾⣏⣷⡿⣏⣷⣿⣿⢷⠀⠀⡇⢸⣿⢿⣇⠈⢿⢸⡇⠈⢸⣷⠇⢸⣰⣿⡿⣏⣿⢿⣾⡿⣷⣏⣿⢷⣿⡾⣷⣿⣹⣷⣿⣏⣷⣿⣹⢿⡾⣏⣿⣏⡿⣷⣿⡾⣷⡿⣿⣿⣿
            ⣿⣷⣻⢿⣽⣻⢷⣯⡿⣽⣿⣷⣯⣟⣿⣽⣾⣿⣽⣾⣟⣾⣽⣻⣽⣾⣻⣷⣿⣽⣻⣷⣟⣿⣽⣾⣟⠘⣇⣀⢳⣾⢻⢼⡟⠀⣈⣸⠁⢀⢾⠟⠆⢸⣿⣯⣟⣿⣽⣿⡞⠙⠛⣽⠞⠛⠓⠛⠛⠚⠓⢿⣾⣽⣾⣳⣿⣯⣿⣻⣷⣯⢿⣻⡾⣽⡿⣽⣷⣻⢿
            ⣿⣷⣻⣯⣷⣟⡿⣞⣿⣳⣿⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠀⠈⠁⣯⣀⣙⣈⡟⣅⣸⡞⢧⣬⢿⡟⢧⡟⢿⣀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢀⡀⠀⠁⠀⠈⠀⠉⢙⣿⣟⡷⣿⢯⣟⣷⣻⣽⣿
            ⣿⣷⣻⢷⣻⣾⣿⡿⠿⠛⠃⠀⠀⠀⠀⠀⠀⠄⠄⠠⢀⠤⣀⠄⡀⣤⠴⠤⠠⢤⣶⠦⠐⣤⣴⠶⠁⢀⡴⣡⢆⡾⢁⠀⠀⠀⡝⠀⠀⠀⠈⠉⠁⠀⠁⠄⠀⢠⡄⠀⠐⠂⠀⠐⠀⠀⠀⠀⠘⠤⠀⠒⠠⢄⡐⡀⠂⠤⣀⠀⠈⠛⠿⢿⣯⣿⣻⣞⣯⣷⣿
            ⣿⣾⣿⠛⠛⠉⠀⢀⠴⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠁⠀⠀⠠⠋⠀⠀⢀⣴⠋⠁⠀⣼⠋⠁⠀⠀⣘⣷⣧⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠳⡀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠁⠂⠌⠛⢦⣄⠀⠀⠀⠉⢙⣻⣿⣿⣥
            ⣿⣿⠉⢑⣖⣒⠲⠶⠶⠶⢶⣶⣶⣶⣶⣶⣶⣶⣶⢶⠶⠶⠶⠶⠒⠒⡞⠉⠉⣷⣲⣾⣷⣾⣯⣽⣿⣿⣿⣿⣾⣾⣿⣽⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⣿⣶⣺⣿⣖⠉⠙⣶⣲⡶⠶⠶⠿⢶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠾⠿⠾⠓⠛⠉⠉⢻⣾⢿
            ⣿⡇⠀⢸⣿⣿⣟⣾⣲⡛⣺⣿⠙⣟⣶⢳⣶⡗⠸⡆⣿⢗⣿⣾⣿⣿⢟⠀⠀⣿⢿⡿⠋⡉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⢉⢚⡟⠀⠈⣿⣽⡽⣿⡗⡞⣛⣿⠈⣷⣳⢿⣴⣶⠀⡆⢸⡗⣺⡞⣿⣿⣿⠀⠀⢸⣿⣿
            ⣿⣷⣤⣤⣏⣭⣬⣥⣁⣉⣉⣉⣈⣁⣈⣋⣉⣑⡀⠉⠉⣉⣁⣉⣍⣉⣉⣀⡤⣱⠋⠀⠀⡄⠀⣿⣿⣿⡿⣽⣿⣯⣿⣻⣿⣿⣿⡿⣿⣻⣿⣿⡿⣿⣿⣿⠀⠀⣤⣴⣷⣤⣤⣼⣿⣠⣁⣈⣈⡉⠉⠀⠁⡈⡛⣙⣈⣂⣉⣉⣁⣉⣉⣉⣉⣉⣀⣠⣾⣿⢿
            ⣿⣿⣿⣿⠅⢹⡇⢬⣿⢿⣏⠻⢿⡍⢿⠁⠠⠄⠤⠀⠤⠤⠠⡇⢸⠀⠀⠈⣴⡋⠈⠀⠀⡇⠀⡿⣽⣿⡇⢿⣿⣳⣯⡿⣟⡷⣻⡿⣿⣽⣿⣿⠇⣿⣿⣻⠀⢸⣿⣿⣿⡿⣿⣿⢿⣽⠀⠩⢭⠉⠉⠀⠁⠁⠃⢸⡇⠰⠤⠤⠄⠀⠠⠤⣯⠀⢸⣿⣿⣿⣿
            ⣿⣿⣿⢿⠂⢸⣿⣚⠿⠀⢿⡼⣻⡆⣼⠀⡅⠀⠀⢀⢀⠀⢀⡇⢸⠀⣛⡾⠁⠈⠃⠐⣴⡇⠀⡇⣿⣿⣧⢻⣽⣿⣼⣿⣟⢯⣿⣵⣯⣿⣿⣿⠀⣿⣿⢸⠀⣿⣿⡋⠻⣧⣾⣾⣿⢻⠀⡔⠒⠒⠒⠒⠒⠂⡃⢸⠆⢘⠁⠀⣀⣈⢁⣀⣻⣤⣾⡏⠿⢋⢻
            ⠗⣸⠛⣾⡅⣸⠷⠾⠶⠤⣤⣧⣼⡇⢽⠐⣷⣶⣦⠀⠀⠤⢶⣷⢸⠀⡧⠄⠀⠀⢰⠆⠀⣇⠀⠃⣿⣿⠙⣿⣶⣶⣶⣿⣿⣋⣿⣶⣶⢶⣿⡏⠀⣿⣿⠰⠀⢻⠿⡷⡌⠽⠿⠿⣾⢿⠀⢡⣴⣂⣀⣀⣀⣀⡍⢸⡀⢱⣤⣤⡄⠀⣿⣋⡗⢻⡟⣷⣎⠀⠌
            ⠐⢠⣿⣿⡇⣸⡦⢀⡀⠀⣰⡍⡙⢳⣿⣶⠀⠉⢨⣦⣤⣤⠊⠀⣿⣿⣿⠁⠀⠀⠀⠈⡌⠏⠀⣶⢹⣿⠀⠕⣻⣞⣿⣿⡇⠀⣻⣿⣿⣿⡟⠀⠀⣿⣿⢸⢆⠉⠉⢉⣭⡭⢭⠉⠉⣿⣶⣁⡀⠀⠀⠀⠉⠉⠓⢼⣣⡏⠈⠉⠀⠀⡿⢤⠫⡝⡁⢻⣿⡌⡐
            ⡠⠞⣾⣹⡇⠿⢿⣶⣷⡿⣝⢻⣷⣤⣿⣷⣄⢶⣲⢿⣳⡟⡖⠀⣿⣿⠿⣷⠀⠐⣠⣴⣿⣗⢲⢂⣸⣿⠀⠀⠈⠉⠉⠉⠁⠀⠈⠁⠉⠉⠁⠀⠀⣸⣿⣸⣿⠀⢶⣾⣿⣶⣶⣖⠂⣿⣿⡏⠛⠛⢳⣖⡲⣖⣶⣿⡿⢿⣷⣴⣾⣷⡉⠒⠃⡥⢣⣋⣿⣯⡹
            ⢱⠈⣿⣾⠇⡶⡾⢿⣿⢿⣿⠿⣹⣿⣿⣿⡿⣿⣸⣾⣿⣹⡿⠀⠷⣿⢇⣿⡀⢶⣿⣿⢿⣿⣿⣾⡏⡀⠆⡆⡰⢀⠆⣀⠰⡀⢆⠰⣀⠀⡆⢀⡀⢰⢸⣏⣿⣀⣉⣉⣇⣉⣉⣉⣀⣿⣿⡇⠀⢀⣰⡿⠿⣾⣿⣿⢿⣹⣿⣿⣱⣾⣿⡆⠀⡏⣹⡿⣾⣹⢇
            ⣢⡽⠴⡹⠶⠷⠲⠧⠶⠦⠶⢶⣾⣿⣿⣿⣃⣿⣿⡟⣿⣻⡃⠀⠀⣿⡸⣼⣇⣈⣿⣿⣿⣿⣿⣿⣷⣬⠓⠦⠳⠍⠒⠂⠓⠘⠂⠓⠦⠽⠴⠣⠼⠦⢍⠧⠯⠽⡹⠜⡛⠛⠛⠛⠾⠿⣿⣇⣴⡿⣟⣶⡿⢾⣿⣽⣿⣳⣿⣿⣯⣿⣿⣿⠀⣽⢿⣽⣟⠧⢿
            ⠠⢄⡡⢜⡱⣘⠧⡵⢚⠚⡍⢆⣡⠙⣌⠙⡛⢛⢛⠻⡛⢟⡛⠟⣛⢛⡉⢉⡉⢉⣉⡉⠉⣉⠉⢉⡉⠉⣉⢁⣀⢈⡁⣈⠠⢃⠎⣑⠒⡰⢂⡍⢆⠓⡌⠦⡑⠦⢱⢨⡑⣉⠦⡑⢄⢂⡈⠟⡻⠿⠻⠞⡝⢣⠙⣋⠛⣛⠻⢍⠩⢍⠍⣍⢋⠹⢌⢢⡐⡠⢠
            ⣱⣈⣀⣠⢦⡱⣒⡬⣥⢎⣔⣣⢤⣓⢬⣱⢩⡜⣌⣲⣡⢎⣥⡚⠄⢎⡔⣢⡜⣤⢆⡴⣣⡔⣬⡒⣤⢣⣆⡲⣄⡲⣌⣔⣢⣍⡲⣌⣲⢡⣒⣌⣆⡳⣌⣲⣡⢎⣔⣢⣔⣢⢆⣍⠦⣦⣘⣬⡱⣌⡥⣓⢬⣡⢧⣌⣍⢦⣍⡬⣎⣌⢮⡤⣍⠮⣜⣢⣱⢬⣍
            ⣟⣯⣿⣽⣻⢿⣻⠿⣽⣻⢾⡽⣯⣟⣯⣟⣯⢿⣻⢯⣟⣯⢷⣻⢶⡾⣽⢶⣟⣯⣟⡿⣽⣻⣟⡿⣯⢿⣽⣻⣽⣻⡽⣞⡷⣯⢿⡽⣯⢿⡽⣾⢽⣻⣽⣳⢯⣟⣯⢿⣹⢯⣟⣿⣻⡟⣿⢯⣟⣿⣻⡟⣿⣻⡟⣯⣟⣿⡻⣟⣿⣻⢿⡿⣿⣿⣿⡿⣿⢿⣾
            ⣿⣳⢷⡾⣽⢯⣟⢿⣳⢯⣟⣳⡟⣾⣵⡻⣞⣯⢯⣟⡾⣽⣫⢯⣟⡾⣽⡻⣞⡷⢯⣟⡷⣻⢾⡽⣟⡿⣼⣳⢷⣫⡽⣯⡽⣞⣯⣽⣳⢯⣟⡾⢯⡷⢯⣟⡿⢾⣭⠿⣽⣛⡾⢧⣿⣹⡟⣾⡽⣞⣳⣟⢷⢯⣻⢷⣛⡾⣽⡻⣞⣽⣳⠿⣽⢯⡷⣿⡽⣻⣞
            ⣯⡟⣯⣟⡾⣟⡾⢯⣽⣛⡾⣳⣻⢧⡷⣻⣽⣚⣯⠾⣝⣳⢯⡟⣾⣹⣗⣻⡽⣞⣟⡾⣹⢯⢷⡻⣝⡿⣳⢯⣯⢗⣿⣱⢿⣹⢮⣗⣯⣻⢮⣟⢯⣽⡻⣞⣽⣛⡾⣛⣷⣫⢟⣟⡶⢯⣽⡳⣏⡿⣵⡞⣯⡟⣧⢿⣹⡽⣳⣻⢽⣺⣭⠿⣽⢾⣹⣗⣻⡗⣯""")
        print(Fore.BLUE + "1. Pedir un batido radioactivo.")
        print(Fore.BLUE + "2. Retar a la camarera a un concurso de gritos.")
        print(Fore.BLUE + "3. Comer un plato de alas picantes nivel Cartman.")
        print(Fore.BLUE + "4. Intentar robar el sombrero de un cliente.")
    elif escenario_actual == 2:  # Casa de Cartman
        print(Fore.LIGHTBLUE_EX + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠋⠁⠀⠀⢹⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⠶⠶⣦⣄⣀⣠⣾⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣿⣷⣶⣶⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⣿⣿⣿⣦⣀⣤⣴⡾⠟⠋⠉⠀⠈⠙⣿⣷⡄⠀⠀⣀⣠⣤⡶⠿⠿⠷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⡿⢿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠈⠙⠻⢷⣦⢀⣀⣠⣶⣿⣿⣉⣁⣀⣈⣽⣿⣦⣀⡀⠀⠀⠀
            ⠀⣀⣠⣤⣶⣾⣿⣿⣿⡿⠛⠁⠀⠈⠙⣻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⢠⣄⠀⠀⠸⣿⣷⣝⢻⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣄⣤⣤⣤⣤⣤⣤⣴⣶⣶⡾⡿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦
            ⣿⣿⣿⣿⣿⣟⣿⣿⡿⠿⠿⠿⣶⣶⡿⢿⣷⣿⣿⡇⠀⠀⢸⣿⠿⣿⠿⣿⠀⢸⣿⡿⣿⠿⣿⠁⢰⣿⠿⣿⢿⣿⡇⠀⠀⣿⣿⣿⣿⠿⠛⠉⠉⠀⠈⠉⠉⠀⠉⣩⣿⣿⣿⣿⣿⣿⣍⠉⠀⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠌⠉⠉⢹⣏⡉⣿⠿⢹
            ⣿⠉⠻⣿⣿⣿⣿⣿⠁⠀⠀⠀⠈⠀⠀⣼⣿⠏⣿⡇⠀⠀⢸⣿⣤⣿⠀⣿⠀⢸⣿⣿⣿⡄⣿⠀⢸⡇⢤⣿⢰⣿⣧⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⠟⠉⠈⢻⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣇⡀⠀⠐
            ⣿⠀⢠⠘⣿⣿⣿⡏⠀⠀⣴⠀⣴⣦⣤⣿⣿⠃⣿⡇⠀⠀⣸⣿⣦⣿⣠⣿⠀⢸⣿⣦⣿⣤⣿⠇⢸⣷⣤⣷⣀⣿⣿⠀⠀⣿⡇⢀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣷⣄⠀⠀⠀⠀⠀⡄⡄⠀⣀⣴⣾⣟⣿⡿⢿⣿⣿⣦⣀
            ⣿⠀⠾⠃⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣾⣿⣧⡄⣿⡇⠀⠀⠉⠛⠋⠉⠉⠛⠀⠀⠉⠉⠉⠉⠉⠀⠈⠉⠋⠉⠙⠛⠻⠀⠀⣿⣧⣼⡀⠀⠀⢀⣴⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣦⣀⣾⠀⢀⣴⣾⢟⣽⣿⠛⠛⠀⠀⠙⠿⢿⣿
            ⣿⡀⢀⣰⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣶⣾⣿⣿⡟⢋⡁⡀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⣀⣀⣀⣘⣿⣿⣿⣿⣿⣿⣯⣿⡿⠟⠁⠀⠀⠀⠀⠀⠛⠛⢻
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⢿⣿⣿⢿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣀⣠⣶⣶⣶⣶⣶⣶⣤⣄⡀⠀⠀⢀⡀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⠋⠀⠈⠁⠁⠀⠈⠉⠉⠉⠉⠉⠉⠉⠀⠀⠉⠉⠉⠉⠉⠙⢻⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⣠⣤⣼
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⢻⣿⣶⣿⣇⠀⠀⢰⣿⠿⣿⡟⣿⣿⣿⡿⢿⣿⡿⢿⣿⣿⡟⢻⡟⠻⣿⡀⠀⣿⣿⣹⣿⣿⣿⣿⡏⠀⢰⣶⣤⣤⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⣿⣿⣿⡿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢰⣯⣽⣿
            ⣿⣿⣿⣿⣿⣿⣿⣷⡍⣵⣼⣿⡿⢟⣸⣷⣿⢿⣙⣿⡀⠀⢸⣿⠀⣿⡇⢸⡇⣿⡇⢸⣿⡄⢸⣿⢸⡇⠰⡷⢶⣿⡇⠀⢻⣿⡟⢻⣿⣽⣿⡇⠀⢸⣏⣭⣍⣉⣉⣉⣉⣉⣉⣉⣭⣉⣉⣉⣩⣭⣭⣽⣿⠀⣿⣿⣟⣻⣻⣿⡆⠀⠀⣀⠀⢀⢠⣿⣿⣟⣿
            ⡏⣭⠉⢉⠉⠉⠛⠛⠛⠋⠛⠛⠛⠛⢿⡿⠿⣿⣿⣿⠁⠀⢼⣿⣆⣿⣧⣼⣧⣿⡇⠘⠛⢻⣾⣿⢸⣷⣼⣧⣤⣿⡇⠀⢸⣿⡛⠛⠛⠛⣸⣿⠀⢸⡇⣾⡷⠶⠶⠾⠿⠴⠰⠶⠦⠶⠿⠰⠏⠈⠿⢿⣿⠀⣿⣏⠿⠛⠛⠛⡛⢛⢻⣿⢿⣿⣟⡛⠛⠛⠿
            ⡇⣼⠀⣾⣶⣶⣤⣤⣤⡆⠀⠀⠀⠀⢸⣷⣾⣿⣿⣿⣆⣀⣀⣩⡍⠉⠉⠉⠁⣿⡇⠀⠀⠘⢿⣿⠀⠈⠉⠉⠉⠉⠀⠀⢸⣿⣿⣷⣶⡿⣿⣿⠀⢸⡟⣛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⡟⣿⠀⣽⣿⣿⣶⣶⡄⠛⠸⠿⡇⣿⣿⣿⣿⡇⠀⠀
            ⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⠀⠀⠀⣠⣿⣇⣀⣀⣀⣸⣿⣀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡇⠀⢸⣧⣼⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣴⣿⣿⣿⣿⣿⣷⣤⣤⣶⣷⣿⣿⣿⣿⣿⣷⣿
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⣿⣿⣤⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⢸⣿⣿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣶⣿⣿⣿⣏⣿⡿⣿⣿⣿⣿⣍⣉⠉⠉⠻⠿⠟⠁⠀⠈
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⣠⣶⣿⡟⠛⠛⠛⠛⠋⠉⠉⠉⠙⠻⣿⣍⠉⠉⠙⠻⣿⣭⣉⣛⣿⡿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠛⠛⢛⣿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠘⠛⠛⢛⠛⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣷⣦⣀⡀⠈⠉⠙⠛⠛⠻⠿⠿⠷⠶⠶⠶⣶⣶⣶⣶⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠉⠉⣡⣄⣀⣴⣶⣬⣤⣤⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠷⠶⠶⠶⢶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⡀⠉⠛⠛⠻⠛⠙⠋⠉⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠛⠛⠛⠛⠿⠶⠶⠶⢶⣶⣶⡾⠛⠛⠛⠛⠛⠛⠛⠛⣿⠟⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⣷⡾⠛⠛⠛⠛⠛⠛⢛⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣟⠛⠛⠛⠛⠛⠛⠛⢻⣿⠛⠛⠓⠚
            ⣀⣀⣀⣀⣤⣤⣤⣾⣛⣍⣥⣄⣀⣀⣀⣀⣀⣠⣾⣋⣀⣀⣀⣀⣠⣤⣤⣤⣤⣾⣏⣁⣀⣀⣀⣀⣀⣀⣀⣠⣾⢋⣀⢀⣀⣤⣠⣤⣤⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⣀⣀⣀⣀⣀⡀⢀⢙⣧⣀⣀⡀""")
        print(Fore.BLUE + "1. Encender la barbacoa con gasolina.")
        print(Fore.BLUE + "2. Probar el nuevo experimento químico de Kenny.")
        print(Fore.BLUE + "3. Comer toda la comida del refrigerador.")
        print(Fore.BLUE + "4. Llamar a la mamá de Cartman para una pelea.")
    elif escenario_actual == 3:  # Terreno Baldío de los Chicos
        print(Fore.LIGHTBLUE_EX + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠈⠹⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠉⠓⠦⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣴⡏⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠈⠑⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣀⣤⣴⣾⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣶⣦⣶⣴⣶⣶⣶⣶⣦⣤⣤⣴⣶⣶⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⢿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⣿⣿⣿⣿⡿⠏⢷⣄⡀⢴⡘⢿⣿⣿⣿⡿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣶⣤⠴⣻⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠷⢿⣿⣿⣿⣿⣽⣿⣿⣟⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⣿⣿⣿⣿⣤⢴⡿⡿⣯⣿⣅⣠⣿⣿⣿⣟⣿⣿⣟⣿⣿⣿⣯⣿⣿⣿⣛⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣿⣿⣿⢀⣸⣿⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣤⣄⣀⣀⣀⡀⠀⠀⠀⠀⠀
            ⣿⣿⣿⣿⣿⣿⣿⣿⣀⠃⠀⣻⣼⣿⠉⣿⣿⠁⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣿⣿⣿⣟⣋⡟⢻⣿⣿⣧⣴⣿⣿⡿⣾⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣅⣀⣿⣿⣷⣾⣏⠉⢡⡀⢿⣿⣿⢻⣿⡧⢾⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣾⣿⣿⣍⠙⣅⢸⣿⡿⠵⠆⢹⣿⡏⠉⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⠷⢒⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⢿⣿⣿⣾⣿⣭⡽⠉⣿⣿⡟⠉⡇⠘⢿⠏⢯⢩⣤⣟⠚⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣷⣿⠿⠶⢾⠀⢿⡋⢹⡀⠹⢗⣙⣿⡆⢲⣼⣿⢗⡻⠻⣿⣿⣿⣿⣿⣿⣻⣿⣿⣯⣷⣿⣿⣿⣿⣿⣿⣷⣏⡉⢩⡀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⢿⣿⣿⣿⠿⠄⠴⣦⡹⣿⣷⣶⣿⠅⢠⠾⠿⣆⢙⡏⡇⠻⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⠿⠛⡇⠘⢿⠌⣻⢿⠿⠀⠾⠛⢻⣷⠀⣸⢮⡍⣡⡄⢻⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣀⣭⡄⠙⣁⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿
            ⣠⣿⡿⢤⣦⣶⠆⢠⣶⣼⡇⡄⢉⣦⠀⣠⣰⣿⠉⠛⠋⠐⠉⢻⣿⣿⣿⣿⣿⣻⣽⣿⣿⣿⣟⣿⠗⢶⡶⣿⡇⢠⠼⠛⠃⠘⠁⠐⠲⠿⢻⡄⢡⣰⣧⠈⢉⣠⣿⣿⣿⣿⣿⣯⣿⣿⣿⠿⠿⠟⠛⠛⠻⠏⠈⠫⠛⣧⠈⣉⣈⣿⣿⡿⠿⠟⠛⠛⠉⠉⠉
            ⠉⠉⠁⠀⠀⠀⠀⠀⠿⠿⡿⢿⠏⠉⠉⠹⢿⠿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠹⠿⠿⠿⠿⠉⠉⣷⣶⣀⡇⢰⣿⣀⣰⣶⣿⠇⠀⠀⠀⠀⠀⠀⠈⠉⠏⠀⠉⠀⠈⠿⠏⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠈⠉⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
        print(Fore.BLUE + "1. Construir una rampa para bicicletas con restos oxidados.")
        print(Fore.BLUE + "2. Encender fuegos artificiales dentro de una cueva.")
        print(Fore.BLUE + "3. Saltar desde una grúa hacia un charco.")
        print(Fore.BLUE + "4. Escalar un árbol lleno de abejas.")
    # validamos la opcion elegida
    opcion_elegida = int(input())
    while opcion_elegida < 1 or opcion_elegida > 4:
        print(Fore.RED + "Opción no válida. Elige un número entre 1 y 4.")
        opcion_elegida = int(input())

    # mostramos las opciones por pantalla dependiendo de la respuesta del usuario
    if escenario_actual == 1:
        if opcion_elegida ==1:
            puntos += 10
            print(Fore.GREEN + "El batido explota en tu estómago, provocando que te desintegres en una nube de colores radioactivos.")
            print(Fore.GREEN + "Cartman se ríe a carcajadas: ¡Eso sí que fue épico!")
            print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠚⠉⠓⠋⠓⠤⠦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢁⣠⣶⣀⣤⣄⣠⣤⡤⠏⠙⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠋⠁⠈⠉⠀⢀⠀⡀⢀⠀⠀⠀⠄⠂⠠⠀⠄⠀⠉⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠠⠀⢂⠠⠁⢈⠀⠄⠠⠀⠂⢁⠈⠀⠄⠁⡀⠂⢁⠈⠀⠄⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠁⢀⠂⠁⡀⠂⡀⢤⣐⣀⣀⣢⡴⠤⠥⠶⠶⠷⢶⣶⠾⠦⢤⣤⣁⣀⣂⠀⠹⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡞⠁⠀⠂⢀⣂⣤⠴⠖⠛⣉⣉⣻⠶⣤⣴⠖⠒⣶⠾⠿⢶⣒⠒⠒⠲⠤⠬⢍⣙⣓⠻⢦⠀⠀⠀⠀⠀
⠀⠀⠀⣼⠀⣠⡥⠞⠋⣉⡤⠴⢒⡿⠋⠀⠀⠀⠀⠙⢦⡞⠁⠀⠀⠀⠈⠙⢦⠀⠀⠀⠀⠀⠈⠉⢻⠀⠀⠀⠀⠀
⠀⠀⢰⡷⠛⣁⠴⠒⠉⠁⠀⠀⡞⠀⠀⠀⠀⠀⢀⣄⢸⣇⣄⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀
⠀⠀⢻⡔⠋⠁⠀⠀⠀⠀⠀⢐⡇⠀⠀⠀⠀⠀⠈⠁⡼⣎⠁⠀⠀⠀⠀⠀⠀⣹⠀⠀⠀⠀⠀⠀⢨⠇⠀⠀⠀⠀
⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⢠⡼⠁⠘⢦⣀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀
⠀⠀⢠⣼⣆⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⠤⠖⠚⠁⠀⠀⠀⠀⠈⠉⠒⠒⠋⠁⠀⠀⠀⠀⠀⣤⢰⣧⡀⠀⠀⠀⠀
⠀⣰⣿⣻⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣠⠞⣡⣿⣻⢿⣷⡄⠀⠀
⢠⣿⢷⣯⣟⡿⣷⡳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⡤⢤⠤⣶⠞⠁⠀⠀⠀⢀⡤⠞⣡⣼⣟⡷⣯⣟⡾⣿⡄⠀
⣼⣿⣻⢾⣽⣻⣽⣻⣶⣍⡓⠦⣄⣀⠀⠀⠀⠀⠠⠬⣭⣿⠭⠴⠖⢀⣠⠴⠚⣉⣴⡾⣟⡷⣯⣟⡷⣯⢿⡽⣿⡀
⣿⣳⢯⣟⣾⣳⢯⡷⣯⣟⡿⣷⣦⣬⣍⣓⣒⢲⡶⠖⠚⠳⡖⠺⢯⣭⣴⣶⡿⣟⣯⢿⣽⣻⢷⣯⢿⡽⣯⢿⡽⡇
⢹⣟⡿⣞⡷⣯⢿⣽⣳⢯⣟⡷⣯⢷⣻⣟⣿⡏⠀⠀⠀⣴⠃⠀⠀⢻⡷⣯⢿⡽⣞⡿⣾⣽⣻⣞⣯⢿⡽⣯⣟⣷
⠘⣿⡽⣯⢿⣽⣻⢾⣽⣻⢾⡽⣯⣟⣷⣻⢾⡇⠀⠀⢀⡬⠟⠀⠀⢸⣿⡽⣯⢿⣽⣻⢷⣯⢷⣻⣞⣯⣟⡷⣯⡿
⠀⣿⡿⣽⣻⢾⣽⣻⢾⡽⣯⣟⣷⣻⢾⣽⣻⢿⣤⣀⢀⡽⠀⢀⣠⣿⡿⣽⢯⣟⡾⣽⣻⣞⣯⢷⣻⢾⣽⣻⣷⠃
⠀⠈⢻⣷⣯⣟⣾⡽⣯⣟⣷⣻⢾⣽⣻⢾⡽⣯⣟⡿⣿⣿⣿⣿⣟⣯⢿⣽⣿⣾⣿⣷⣿⣾⣿⣿⣿⣿⣾⠋⠀⠀
⠀⠀⠘⣿⣿⣿⣿⣿⣷⣿⣾⣯⣿⣾⣽⣯⣿⣷⣯⣿⣷⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣽⠏⠀⠀⠀
⠀⠀⣠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⠀⠀⠀""")
            pygame.mixer.music.load("musica proyecto/dumb_ways.mp3")
            pygame.mixer.music.play()
            input()
        else:
            vidas -= 1
            if opcion_elegida == 2:
                print(Fore.BLUE + "La camarera grita tan fuerte que revienta los tímpanos de todos. Kenny, sin saber por qué, explota.")
                print(Fore.BLUE + 'Kyle dice: "¡Dios mío, mataste a Kenny!" Stan responde: "¡cabronazooos!" ')
                print(Fore.LIGHTMAGENTA_EX+ """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⣴⢚⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⠤⠤⢀⣀⡀⠀⠀⠀⠀⠃⡴⣻⠋⡟⢠⡇⡾⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠊⢡⠀⠂⡄⠂⡄⠂⠉⠒⣤⠀⡆⣾⢱⠃⣼⣥⣾⣿⡟⢹⢫⣾⠛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢊⠐⣈⣴⠶⠛⠛⠛⢿⣶⣶⣈⠌⠳⣿⣿⡿⣿⣟⣻⢷⣮⠽⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⠀⣀⠀⠀⡸⢁⠂⣼⣿⡁⠄⡀⡐⠉⠈⠉⢾⢹⣧⡀⠹⡄⠉⠑⠺⠛⠉⠀⠴⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠃⡘⢷⣴⠃⡆⣾⢳⡏⠀⠀⠿⡇⠀⠀⠀⠈⢧⢻⣷⠀⢻⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡤⠤⠤⣭⣿⣿⡎⡱⣿⡹⡇⠀⠀⠀⠐⡀⠆⠀⠀⢸⣼⢿⠂⣽⣀⣴⢋⢦⢹⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣷⣴⣾⠏⢉⡽⡹⢧⠀⢿⣷⡹⣄⠀⠀⠀⡘⠐⠀⠐⣟⡞⡼⢁⡾⠀⢺⣜⡊⣾⡃⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣾⣿⢿⡾⣷⣶⣾⠁⠁⠸⡇⠈⣇⠹⣎⣷⡆⠈⠀⠀⢀⣾⠏⣰⠇⣾⢁⡾⠉⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠼⠿⠛⠛⠛⠛⠛⢋⡧⢴⠤⣀⣘⣦⡈⠳⢌⡉⠙⠛⠒⠛⣯⣤⠞⣡⠞⠁⡘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢺⡌⢧⠹⡌⣧⠠⠉⠓⠦⢭⣍⣛⣛⣩⡽⣼⠛⠥⠄⠡⢀⠈⢧⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠣⢳⣎⣽⠓⠛⠓⠻⡄⡀⠂⠄⠠⢀⠉⢷⡀⠌⡀⢂⡴⠞⠉⠉⢉⣾⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢱⡀⠡⢈⠐⢀⠂⢀⢳⣠⠖⠋⢀⠂⠌⡀⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠲⠆⠖⠒⠛⠉⡉⡤⠚⠉⠉⠓⠒⢼⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠘⢀⠃⠘⠠⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣦⣄⣌⣤⣡⣶⣾⣿⣤⣤⣤⣤⣤⣴⣶⣶⣶⣦⣦⣤⣤⣀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⢿⠿⠿⠿⠿⠿⠻⠛⠛⠛⠛⠉⠉⠉⠁⠉⠉⠀⠀""")
                pygame.mixer.music.load("musica proyecto/O Dios Mio Han Matado a Kenny Hijos De Puta (mp3cut.net).mp3")
                pygame.mixer.music.play()
                input()
            elif opcion_elegida == 3:
                print(Fore.BLUE + "Las alas son tan picantes que expulsas fuego por la boca. En lugar de morir, incendias el restaurante y sales corriendo en llamas.")
                print(Fore.BLUE + 'Cartman comenta: "¡Eso fue lamentable! Yo habría aguantado el picante."')
                pygame.mixer.music.load("musica proyecto/Alerta.mp3")
                pygame.mixer.music.play()
                input()
            elif opcion_elegida == 4:
                print(Fore.BLUE + "El cliente es miembro de un club de peleas clandestino. Te da una paliza épica, pero sobrevives con un ojo morado.")
                print(Fore.BLUE + "Cartman se rie tanto que le da un ataque de asma mientras stan le da 10 pavos a kyle por tu derrota")
                pygame.mixer.music.load("musica proyecto/Alerta.mp3")
                pygame.mixer.music.play()
                input()
    elif escenario_actual == 2:
        if opcion_elegida ==2:
            puntos += 10
            print(Fore.GREEN + "Te conviertes en una especie de mutante fluorescente que brilla durante unos segundos antes de explotar en mil pedazos.")
            print(Fore.GREEN + 'Cartman: "Eso es lo que yo llamo dedicación."')
            pygame.mixer.music.load("musica proyecto/dumb_ways.mp3")
            pygame.mixer.music.play()
            input()
        else:
            vidas -= 1
            if opcion_elegida == 1:
                print(Fore.BLUE + "La explosión lanza a Kenny por los aires. Su aterrizaje termina con un satélite aplastándolo.")
                print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⣴⢚⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⠤⠤⢀⣀⡀⠀⠀⠀⠀⠃⡴⣻⠋⡟⢠⡇⡾⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠊⢡⠀⠂⡄⠂⡄⠂⠉⠒⣤⠀⡆⣾⢱⠃⣼⣥⣾⣿⡟⢹⢫⣾⠛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢊⠐⣈⣴⠶⠛⠛⠛⢿⣶⣶⣈⠌⠳⣿⣿⡿⣿⣟⣻⢷⣮⠽⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⠀⣀⠀⠀⡸⢁⠂⣼⣿⡁⠄⡀⡐⠉⠈⠉⢾⢹⣧⡀⠹⡄⠉⠑⠺⠛⠉⠀⠴⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠃⡘⢷⣴⠃⡆⣾⢳⡏⠀⠀⠿⡇⠀⠀⠀⠈⢧⢻⣷⠀⢻⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡤⠤⠤⣭⣿⣿⡎⡱⣿⡹⡇⠀⠀⠀⠐⡀⠆⠀⠀⢸⣼⢿⠂⣽⣀⣴⢋⢦⢹⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣷⣴⣾⠏⢉⡽⡹⢧⠀⢿⣷⡹⣄⠀⠀⠀⡘⠐⠀⠐⣟⡞⡼⢁⡾⠀⢺⣜⡊⣾⡃⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣾⣿⢿⡾⣷⣶⣾⠁⠁⠸⡇⠈⣇⠹⣎⣷⡆⠈⠀⠀⢀⣾⠏⣰⠇⣾⢁⡾⠉⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠼⠿⠛⠛⠛⠛⠛⢋⡧⢴⠤⣀⣘⣦⡈⠳⢌⡉⠙⠛⠒⠛⣯⣤⠞⣡⠞⠁⡘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢺⡌⢧⠹⡌⣧⠠⠉⠓⠦⢭⣍⣛⣛⣩⡽⣼⠛⠥⠄⠡⢀⠈⢧⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠣⢳⣎⣽⠓⠛⠓⠻⡄⡀⠂⠄⠠⢀⠉⢷⡀⠌⡀⢂⡴⠞⠉⠉⢉⣾⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢱⡀⠡⢈⠐⢀⠂⢀⢳⣠⠖⠋⢀⠂⠌⡀⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠲⠆⠖⠒⠛⠉⡉⡤⠚⠉⠉⠓⠒⢼⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠘⢀⠃⠘⠠⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣦⣄⣌⣤⣡⣶⣾⣿⣤⣤⣤⣤⣤⣴⣶⣶⣶⣦⣦⣤⣤⣀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⢿⠿⠿⠿⠿⠿⠻⠛⠛⠛⠛⠉⠉⠉⠁⠉⠉⠀⠀""")
                pygame.mixer.music.load("musica proyecto/O Dios Mio Han Matado a Kenny Hijos De Puta (mp3cut.net).mp3")
                pygame.mixer.music.play()
                input()
            elif opcion_elegida == 3:
                print(Fore.BLUE + "Terminas vomitando de forma descontrolada. La mamá de Cartman entra furiosa y te obliga a limpiar todo.")
                print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⢀⣴⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⣻⣞⡷⣯⣟⣿⣿⣷⣄⠀⠀⠀⠀
⠀⢠⣿⣿⣟⣾⣷⣯⣟⣷⣻⣿⣿⣯⣿⣦⠀⠀⠀
⠀⣿⡿⠟⠛⣫⠧⠨⢍⣹⠟⠯⣉⠙⠛⢻⡆⠀⠀
⠀⢻⠀⠀⡜⠁⠀⣤⢸⠽⡤⠀⠀⢣⠀⠈⡇⠀⠀
⠀⣞⠀⠀⢧⡀⢀⣠⡾⢣⣄⡀⣀⡜⠀⠀⣷⠀⠀
⠘⣿⡄⠀⠀⠀⠀⠀⠉⠛⠀⠀⠀⠀⠀⣰⡿⠀⠀
⠀⠘⢿⣦⣀⠀⠀⠀⠺⠖⠀⠀⠀⣠⣼⠟⠁⠀⠀
⠀⠀⣠⠻⣁⣉⠐⠂⠒⠐⠂⠂⢉⣠⠟⠲⡄⠀⠀
⠀⢰⠃⠀⠀⠈⠉⠉⠉⠚⠉⠉⠁⠀⢀⠀⠸⡄⠀
⠀⡏⠀⠠⠁⢀⠂⠀⠂⢀⠐⠀⡈⠀⠄⠀⠂⣧⠀
⢸⠇⠀⢲⠆⠀⠠⠈⠀⠄⠀⠂⢀⠐⢾⠄⠀⣹⠀
⢸⠀⡀⣿⠀⠀⠂⢀⠁⠠⠈⢀⠠⠀⢸⡇⠀⣺⠁
⢸⠄⢘⡇⠀⠠⠁⢀⠀⠂⠠⠀⡀⠐⠀⣷⠀⣼⠀
⠈⣧⣼⡇⠀⠄⠐⠀⡀⠂⠁⡀⠠⠐⠀⣿⣤⡇⠀
⠰⠀⠈⢳⡄⠀⠂⡀⠄⠐⠀⡀⠄⣐⣼⠃⠀⠱⠀
⢢⠀⠀⣨⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣟⡀⠀⢠⠇
⠈⠒⠉⢸⣿⣟⣾⡽⣯⣷⣟⡾⣿⣽⣯⠈⠑⠊⠀
⠀⠀⠀⣼⣿⣟⣾⡽⣟⣾⣽⣻⢷⣻⡷⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣻⣞⡿⣯⣷⢯⣟⡿⣽⡿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣽⢯⣟⣷⣯⢿⣯⣟⡿⣿⠀⠀⠀⠀
⠀⠀⠀⢽⣿⢾⣻⣽⡾⣽⣻⡾⣽⣻⣿⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣻⣽⣳⡿⣯⣷⢿⣻⣽⡯⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣽⣳⡿⣽⡷⣯⣿⣻⣾⡇⠀⠀⠀⠀
⠀⠀⣀⣀⣽⣿⣷⣿⣿⣿⣷⣿⣷⣿⣀⣀⠀⠀⠀
⠀⠀⠉⠛⠛⠛⠿⠿⠿⠿⠿⠿⠛⠛⠛⠉⠁⠀⠀""")
                pygame.mixer.music.load("musica proyecto/Alerta.mp3")
                pygame.mixer.music.play()
                input()
            elif opcion_elegida == 4:
                print(Fore.BLUE + "Liane, la mamá de Cartman, acepta el reto, pero su actitud maternal te desarma. Te regaña durante horas y terminas aun  mas deprimido, pero sin morir.")
                print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⢀⣴⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⣻⣞⡷⣯⣟⣿⣿⣷⣄⠀⠀⠀⠀
⠀⢠⣿⣿⣟⣾⣷⣯⣟⣷⣻⣿⣿⣯⣿⣦⠀⠀⠀
⠀⣿⡿⠟⠛⣫⠧⠨⢍⣹⠟⠯⣉⠙⠛⢻⡆⠀⠀
⠀⢻⠀⠀⡜⠁⠀⣤⢸⠽⡤⠀⠀⢣⠀⠈⡇⠀⠀
⠀⣞⠀⠀⢧⡀⢀⣠⡾⢣⣄⡀⣀⡜⠀⠀⣷⠀⠀
⠘⣿⡄⠀⠀⠀⠀⠀⠉⠛⠀⠀⠀⠀⠀⣰⡿⠀⠀
⠀⠘⢿⣦⣀⠀⠀⠀⠺⠖⠀⠀⠀⣠⣼⠟⠁⠀⠀
⠀⠀⣠⠻⣁⣉⠐⠂⠒⠐⠂⠂⢉⣠⠟⠲⡄⠀⠀
⠀⢰⠃⠀⠀⠈⠉⠉⠉⠚⠉⠉⠁⠀⢀⠀⠸⡄⠀
⠀⡏⠀⠠⠁⢀⠂⠀⠂⢀⠐⠀⡈⠀⠄⠀⠂⣧⠀
⢸⠇⠀⢲⠆⠀⠠⠈⠀⠄⠀⠂⢀⠐⢾⠄⠀⣹⠀
⢸⠀⡀⣿⠀⠀⠂⢀⠁⠠⠈⢀⠠⠀⢸⡇⠀⣺⠁
⢸⠄⢘⡇⠀⠠⠁⢀⠀⠂⠠⠀⡀⠐⠀⣷⠀⣼⠀
⠈⣧⣼⡇⠀⠄⠐⠀⡀⠂⠁⡀⠠⠐⠀⣿⣤⡇⠀
⠰⠀⠈⢳⡄⠀⠂⡀⠄⠐⠀⡀⠄⣐⣼⠃⠀⠱⠀
⢢⠀⠀⣨⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣟⡀⠀⢠⠇
⠈⠒⠉⢸⣿⣟⣾⡽⣯⣷⣟⡾⣿⣽⣯⠈⠑⠊⠀
⠀⠀⠀⣼⣿⣟⣾⡽⣟⣾⣽⣻⢷⣻⡷⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣻⣞⡿⣯⣷⢯⣟⡿⣽⡿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣽⢯⣟⣷⣯⢿⣯⣟⡿⣿⠀⠀⠀⠀
⠀⠀⠀⢽⣿⢾⣻⣽⡾⣽⣻⡾⣽⣻⣿⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣻⣽⣳⡿⣯⣷⢿⣻⣽⡯⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣽⣳⡿⣽⡷⣯⣿⣻⣾⡇⠀⠀⠀⠀
⠀⠀⣀⣀⣽⣿⣷⣿⣿⣿⣷⣿⣷⣿⣀⣀⠀⠀⠀
⠀⠀⠉⠛⠛⠛⠿⠿⠿⠿⠿⠿⠛⠛⠛⠉⠁⠀⠀""")
                pygame.mixer.music.load("musica proyecto/Alerta.mp3")
                pygame.mixer.music.play()
                input()
    elif escenario_actual==3:
        if opcion_elegida ==3:
            puntos += 10
            print(Fore.GREEN + 'Tu salto es tan espectacular que creas un tsunami en el charco y mueres al ser golpeado por los escombros que caen del impacto.')
            print(Fore.GREEN + 'Stan: "¡Eso ha sido la ostiaaa!"')
            print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣶⣾⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣾⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡳⢖⡦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣰⢿⢱⡎⣿⣿⣿⣿⣿⣿⣿⢷⠹⣎⡸⢱⡎⡿⣆⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⠻⣌⢧⢫⡜⢶⡩⢟⡽⣛⠽⣩⢎⡗⢮⡱⢏⡼⣱⢣⡛⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⠻⣌⠷⣩⢎⡳⣜⢣⡝⣎⠶⣙⣎⠳⣎⠞⣥⢛⡜⡲⢥⢧⣙⢦⡛⣦⠀⠀⠀⠀
⠀⠀⢀⡾⣍⠻⣌⡳⡱⢮⡱⢎⡳⡜⣎⢳⡱⢎⡽⣌⠻⣔⡫⢼⡙⣎⠶⣩⢖⡹⣜⣳⡀⠀⠀
⠀⢀⡾⡱⢎⣝⣲⣍⣷⣧⣿⣾⣷⣿⢿⣟⡿⣿⣻⢿⡿⣿⢿⣿⢿⡿⣿⣶⣿⣶⣵⣎⣷⡀⠀
⢀⣼⣷⣿⢿⣟⣿⣻⣟⣿⣿⣳⣟⣾⢯⡿⣽⣷⣻⣯⢿⣽⣻⣿⣿⣻⣷⣻⢾⡽⣯⢿⣻⣷⠀
⢸⣿⣻⢾⣯⣿⣾⣿⠿⠿⠾⠛⠚⠛⠛⠛⡉⠉⠉⠉⠉⠉⠙⠻⢉⠛⠻⠟⠛⠿⠽⠿⣯⣿⡇
⢸⣿⠿⠏⠉⠀⠈⠀⠀⡀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠈⡇
⠈⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⣀⠀⠀⣃⠀⢀⡀⠀⠀⠀⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠁
⢀⠀⠀⠀⠀⠀⠀⠠⡇⠀⠀⠀⠀⠐⠿⠃⠀⣹⠀⠸⠟⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢆⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⡔⠁⠣⡀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠊⠀⠀⠀⠈⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀
⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⠒⡦⡖⢲⠒⡶⢒⡶⠀⠀⠀⠀⠀⠀⠀⡤⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠈⠷⣷⣶⣿⣶⡿⠏⠀⠀⠀⠀⠀⠀⣀⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠟⣳⣄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠿⠉⠀⠀⠀⠀⠀⢀⣠⣶⠟⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⢋⡜⢤⠛⣻⣶⣦⣤⣀⣀⡀⠀⠀⠀⢀⣀⣀⣤⣴⣾⡿⢛⠥⣋⠴⣣⠀⠀⠀⠀
⠀⠀⠀⣸⣃⠎⡜⣶⡉⠖⡤⢍⡛⠿⠿⢿⣿⣿⡿⣿⠿⠿⢟⢫⠱⣌⢣⢚⡤⢓⡜⣧⠀⠀⠀
⠀⠀⢠⡗⡌⢎⣽⠧⡙⡜⡰⢣⠜⣡⢋⢾⡟⣿⡇⢦⡙⢎⡜⢢⠓⡌⢆⣻⡗⣌⠲⡹⡆⠀⠀
⠀⠀⣽⣾⢿⣿⣿⣶⠱⣌⠱⣃⠞⢤⢋⣴⣾⣿⡇⢦⡉⠖⣌⢣⡙⡜⢢⠜⣿⣔⣧⣵⣇⠀⠀
⠀⠀⣿⣯⢿⣿⢾⡿⢒⡌⡓⣌⠚⡤⢣⠼⣉⣿⡎⢦⡙⡜⢤⠣⡜⣌⠣⢻⣿⣟⣯⣟⣿⡆⠀
⠀⠀⠹⢿⣿⣾⡿⢁⡇⡸⢱⠈⢷⡈⢇⠾⣶⣿⠇⣆⢱⠸⡆⢷⠸⣀⠏⡶⢿⣏⣿⣾⣹⡇⠀
⠀⠀⠀⠀⠀⠘⣿⢶⣬⣵⣣⣙⣆⣍⣎⣜⡩⢽⡏⡔⣣⢓⣜⣢⣓⣬⣺⣴⣽⡟⠳⠯⠋⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣊⣞⣱⣫⣽⣩⢯⣹⣹⢛⡟⡻⡝⢯⡻⣭⢏⡽⣩⢳⡜⣲⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠐⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠟⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠷⠤⠄⠀⠀⠀""")
            pygame.mixer.music.load("musica proyecto/dumb_ways.mp3")
            pygame.mixer.music.play()
            input()
        else:
            vidas -= 1
            if opcion_elegida == 1:
                print(Fore.BLUE + "Saltas por la rampa, pero se desmorona al final. Terminas cubierto de basura, y Kenny, que estaba cerca, es empalado accidentalmente por un tubo oxidado.")
                print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⣴⢚⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⠤⠤⢀⣀⡀⠀⠀⠀⠀⠃⡴⣻⠋⡟⢠⡇⡾⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠊⢡⠀⠂⡄⠂⡄⠂⠉⠒⣤⠀⡆⣾⢱⠃⣼⣥⣾⣿⡟⢹⢫⣾⠛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢊⠐⣈⣴⠶⠛⠛⠛⢿⣶⣶⣈⠌⠳⣿⣿⡿⣿⣟⣻⢷⣮⠽⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⠀⣀⠀⠀⡸⢁⠂⣼⣿⡁⠄⡀⡐⠉⠈⠉⢾⢹⣧⡀⠹⡄⠉⠑⠺⠛⠉⠀⠴⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠃⡘⢷⣴⠃⡆⣾⢳⡏⠀⠀⠿⡇⠀⠀⠀⠈⢧⢻⣷⠀⢻⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡤⠤⠤⣭⣿⣿⡎⡱⣿⡹⡇⠀⠀⠀⠐⡀⠆⠀⠀⢸⣼⢿⠂⣽⣀⣴⢋⢦⢹⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣷⣴⣾⠏⢉⡽⡹⢧⠀⢿⣷⡹⣄⠀⠀⠀⡘⠐⠀⠐⣟⡞⡼⢁⡾⠀⢺⣜⡊⣾⡃⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣾⣿⢿⡾⣷⣶⣾⠁⠁⠸⡇⠈⣇⠹⣎⣷⡆⠈⠀⠀⢀⣾⠏⣰⠇⣾⢁⡾⠉⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠼⠿⠛⠛⠛⠛⠛⢋⡧⢴⠤⣀⣘⣦⡈⠳⢌⡉⠙⠛⠒⠛⣯⣤⠞⣡⠞⠁⡘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢺⡌⢧⠹⡌⣧⠠⠉⠓⠦⢭⣍⣛⣛⣩⡽⣼⠛⠥⠄⠡⢀⠈⢧⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠣⢳⣎⣽⠓⠛⠓⠻⡄⡀⠂⠄⠠⢀⠉⢷⡀⠌⡀⢂⡴⠞⠉⠉⢉⣾⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢱⡀⠡⢈⠐⢀⠂⢀⢳⣠⠖⠋⢀⠂⠌⡀⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠲⠆⠖⠒⠛⠉⡉⡤⠚⠉⠉⠓⠒⢼⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠘⢀⠃⠘⠠⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣦⣄⣌⣤⣡⣶⣾⣿⣤⣤⣤⣤⣤⣴⣶⣶⣶⣦⣦⣤⣤⣀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⢿⠿⠿⠿⠿⠿⠻⠛⠛⠛⠛⠉⠉⠉⠁⠉⠉⠀⠀""")
                pygame.mixer.music.load("musica proyecto/O Dios Mio Han Matado a Kenny Hijos De Puta (mp3cut.net).mp3")
                pygame.mixer.music.play()
                input()
            elif opcion_elegida == 2:
                print(Fore.BLUE + "Los fuegos artificiales explotan dentro de la cueva, pero solo logran despertarte murciélagos que te persiguen, uno de ellos te muerde y ahora tienes la rabia")
                pygame.mixer.music.load("musica proyecto/Alerta.mp3")
                pygame.mixer.music.play()
                input()
            elif opcion_elegida == 4:
                print(Fore.BLUE + "Las abejas te atacan. Caen al suelo y empiezan a perseguir a todos. sobrevives, pero lleno de ronchas.")
                print(Fore.BLUE + 'Kyle: "Al menos fue mejor que algunas otras ideas."')
                print(Fore.LIGHTMAGENTA_EX + """⠀⠀⠀⠀⠀⠀⣀⡤⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠤⠤⢤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⠁⡐⢀⠂⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⢁⠐⡀⠂⠄⡈⢷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠐⡀⠂⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⠁⠌⠠⢁⠂⡐⠠⢁⠂⡐⢸⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠰⡏⠐⠤⠡⠌⠤⠡⠌⠤⠡⠌⠤⠡⠌⠤⠡⠌⠤⠡⠌⠤⠡⠌⠴⠀⠦⠠⠁⠆⡐⠠⢹⡃⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡇⢈⡇⡐⠈⡄⠡⠈⡄⠡⠈⡄⠡⠈⡄⠡⢈⠄⠡⡈⠄⢡⠈⠄⣁⠂⠡⢁⠒⢸⡄⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠠⡗⠠⢁⠤⢁⠡⠠⢁⠡⠠⢁⠡⠠⢁⠂⠌⡐⠠⠘⠠⢈⡐⠠⢈⢁⠂⠌⣸⠇⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡟⠋⣇⠁⡂⠰⢀⠂⣁⣢⡶⠇⠌⣠⣁⣂⣌⣐⡠⢁⢧⣅⣂⠄⣁⠂⠂⠌⡐⢸⡇⢾⡀⠀⠀⠀⠀
⠀⠀⠀⣰⠏⢁⠐⣧⣦⡥⠶⠶⠷⠛⡛⠉⠉⠉⠉⣉⠉⠉⢉⠉⠉⠉⠉⢛⡛⠶⠾⠷⠶⣬⣜⠠⢈⠳⡄⠀⠀⠀
⠀⠀⣼⠃⡀⢂⠐⢸⠇⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠈⢳⡔⠁⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⢸⡇⢀⠂⠄⠹⣆⠀⠀
⠀⣰⠃⡐⢀⠂⠌⡾⠀⠀⠀⣸⠁⠀⠀⠀⠀⣤⣀⠀⠈⡇⠀⡄⠀⠀⠀⠀⠀⠀⢧⠀⠀⠈⣧⠀⠌⠠⢁⠹⡄⠀
⢠⡟⠠⠐⠠⢈⣸⠃⠀⠀⠀⡇⠀⠀⠀⠀⠀⠿⠟⠂⢰⡏⠟⠿⠻⠀⠀⠀⠀⠀⢸⡆⠀⠀⠸⡇⢈⠐⡀⠂⢿⠀
⣼⠀⠡⢈⠐⣰⠇⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⣠⠊⠙⢆⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠻⡄⠂⠄⠡⢸⡇
⢿⡌⠐⢠⡼⠃⡀⠀⠀⠀⠀⠀⠙⠦⣄⣀⡠⠤⠚⠁⠀⠀⠀⠙⠦⢤⣀⣠⠴⠊⠀⠀⠀⠀⠀⠀⠙⣎⠠⠁⢬⡇
⠘⣧⣴⠾⠁⠀⢧⡀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⢠⡖⠀⠙⢦⣐⣬⠇
⠀⠁⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣰⡀⠀⠀⠀⢀⠀⣠⡟⠁⠀⠀⠀⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠈⠳⣤⣿⣤⣼⣶⣴⣷⠾⠋⠀⠀⠀⠀⢨⣞⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⢷⣄⡀⠀⠀⠀⠀⠀⠀⠉⠻⢿⡟⠋⠁⠀⠀⠀⠀⣄⣰⣾⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⣋⢮⡝⣻⢶⣤⣄⣀⠀⠀⠀⠀⠈⠁⠀⢀⣀⣤⣴⣾⡿⡟⣭⠾⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⠲⣭⢶⡙⣎⠳⢮⡝⣻⢿⡿⢿⣿⣿⡿⣿⡿⣟⢻⣋⡷⣜⣹⢖⣫⠽⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡿⣜⣣⢧⣿⡹⡜⣿⣷⢾⣷⣾⣟⡵⣻⣿⡱⣷⣿⣻⢷⣿⣷⣍⠾⣏⢶⣋⢿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⣾⣷⣵⣎⣾⠷⡹⣜⣿⣚⣿⣾⢽⡟⣼⣻⣿⡱⣿⣯⣻⣿⣷⣿⢎⣽⣿⢲⠭⡞⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡿⠁⢀⠉⢹⣿⡱⣎⣿⣥⣿⣿⣾⣟⡖⣿⣿⢱⣿⣷⣝⣛⣿⣿⢧⣻⣿⠿⠛⠛⢿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣧⠐⠠⢁⣾⡷⢣⣓⡞⣏⠯⣏⢻⠵⣹⢺⣯⣓⠶⣹⠮⣝⡹⡭⢇⡿⣧⡀⠂⠌⡀⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⠛⠋⠙⣿⣷⣷⣮⣝⣾⣜⣣⣏⣧⢻⣿⣌⣷⣣⣛⣬⣳⣭⣻⣼⡿⠳⣬⠴⠞⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡜⣮⢵⡺⡝⣯⢻⡝⣯⢻⣏⢿⣹⣛⣟⡻⣝⢯⢻⡝⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠓⠲⠿⠿⠿⠾⠿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠿⠿⠷⠿⠾⠷⠿⠿⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀""")
                pygame.mixer.music.load("musica proyecto/Alerta.mp3")
                pygame.mixer.music.play()
                input()

    escenarios[escenario_actual] = ""  # Marcamos el escenario como visitado

# Final del juego
os.system("cls")
if vidas > 0:
    print(Fore.YELLOW + f"""¡Felicidades! Terminaste con {puntos} puntos.
 _____                                                                   _____ 
( ___ )                                                                 ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   | .___________. __    __   _______     _______ .__   __.  _______   |   | 
 |   | |           ||  |  |  | |   ____|   |   ____||  \ |  | |       \  |   | 
 |   | `---|  |----`|  |__|  | |  |__      |  |__   |   \|  | |  .--.  | |   | 
 |   |     |  |     |   __   | |   __|     |   __|  |  . `  | |  |  |  | |   | 
 |   |     |  |     |  |  |  | |  |____    |  |____ |  |\   | |  '--'  | |   | 
 |   |     |__|     |__|  |__| |_______|   |_______||__| \__| |_______/  |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                 (_____)
""")
    pygame.mixer.music.load("musica proyecto/heavens_door.mp3")
    pygame.mixer.music.play()
    input()
    pygame.mixer.music.stop()
else:
    print(Fore.YELLOW + """Te has quedado sin vidas.
 _____                                                _____ 
( ___ )                                              ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |   _______      ___      .___  ___.  _______    |   | 
 |   |  /  _____|    /   \     |   \/   | |   ____|   |   | 
 |   | |  |  __     /  ^  \    |  \  /  | |  |__      |   | 
 |   | |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |   | 
 |   | |  |__| |  /  _____  \  |  |  |  | |  |____    |   | 
 |   |  \______| /__/     \__\ |__|  |__| |_______|   |   | 
 |   |                                                |   | 
 |   |   ______   ____    ____  _______ .______       |   | 
 |   |  /  __  \  \   \  /   / |   ____||   _  \      |   | 
 |   | |  |  |  |  \   \/   /  |  |__   |  |_)  |     |   | 
 |   | |  |  |  |   \      /   |   __|  |      /      |   | 
 |   | |  `--'  |    \    /    |  |____ |  |\  \----. |   | 
 |   |  \______/      \__/     |_______|| _| `._____| |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                              (_____)
""")
    pygame.mixer.music.load("musica proyecto/heavens_door.mp3")
    pygame.mixer.music.play()
    input()
    pygame.mixer.music.stop()


