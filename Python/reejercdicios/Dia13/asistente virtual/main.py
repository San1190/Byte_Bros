from ast import Delete
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep
import os
from os import remove
from pathlib import Path

#path de wikipedia
lugar_archivo = Path('/Users/sanfu/Desktop/Python/reejercdicios/Dia13/guardar_info_wiki')


#programas para abrir
programas = {
    ' discord' :r'C:\Users\sanfu\AppData\Local\Discord\Update.exe --processStart Discord.exe',
    ' chat' : r'C:\Users\sanfu\AppData\Local\WhatsApp\WhatsApp.exe',
    ' lol' : r'"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live',
    ' b alo' : r'"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live'

}

# opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_LAURA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
#escuchar nuestro micro y devolver audio como texto

# escuchar nuestro microfono y devolver el audio comotexto
def trasformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-es")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("ups, no entendi")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"



#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id3)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


#pedir dia de la semana
def pedir_dia():
    dia = datetime.date.today()
    #print(dia)

    #dia semana
    dia_semana = dia.weekday()
    #print(dia_semana)

    
    # diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# informar que hora es
def pedir_hora():

    # crear una variab;e con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)


#funcion saludo inicial
def saludo_inicial():
    #decir el saludo

     # crear variable condatos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    
    
    
    hablar(f'{momento}, soy Neo, tu asistente personal. Por favor, dime en qué te puedo ayudar')



#funcion central del asistente
def pedir_cosas():

    #activar el saludo
    saludo_inicial()

    #variable de corte
    comenzar = True
    
    while comenzar:

        #activar el micro y guardar el pedido en un string
        pedido = trasformar_audio_en_texto().lower()

        if 'abre youtube' in pedido:
            hablar('Recibido, abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
    
        elif 'abre el navegador' in pedido:
            hablar('Entendido, abriendo el navegador')
            webbrowser.open('https://www.google.com')
            continue

        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
    
        
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        
        elif 'gracias' in pedido:
            hablar('No hay de qué, estoy aquí para ayudarte')

        elif 'busca en wikipedia' in pedido:
            hablar("Buscando en wikipedia, espere por favor")

            pedido = pedido.replace('busca en wikipedia', '')
            titulo  = pedido
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 2)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)

            sleep(2)

            hablar("Desea guardarlo en un block de notas?")
            #activar el micro y guardar el pedido en un string
            pedido = trasformar_audio_en_texto().lower()
            
            if pedido == 'si':
                
                nom_arch = titulo + '.txt'
                hablar('Guardando el documento, espere')
                archivo = open(lugar_archivo / nom_arch, 'w' ,encoding='utf-8')
                archivo.write(resultado)
                archivo.close()
                hablar('Guardando con éxito')

                continue

            else:
                hablar("Perfecto, ignoraré la información ")
                continue
            
        
        elif 'borra el documento de' in pedido:
            hablar('borrando el documento, espere')
            titulo = pedido.replace('borra el documento de', '')
            nom_arc = titulo + '.txt'
            archi = Path(lugar_archivo / nom_arc)
            remove(archi)
            hablar('documento borrado con éxito')
            #archi.close()
            continue



            

        elif 'busca en internet' in pedido:

            pedido = pedido.replace('busca en internet', '')

            hablar('Dejame buscarlo por ti')
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue

        elif 'pon en youtube' in pedido:
            hablar('Voy a ello')
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break

        
        elif 'reproduce' in pedido:
            flag = 0
            client_id = "af93b791b15a4b3983a275ca9e0f3a56"
            client_secret = "09be25552e574621a3882d5f8f99cd37"
            autor = '' 
            song = ''
           
            hablar('Entendido')

            song = pedido.replace('reproduce', '').upper()
            flag == 0
            print(song)

            


            
            if len(autor) > 0:
            
                sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
                result = sp.search(autor)

                for i in range(0, len(result["tracks"]["items"])):
                    name_song = result["tracks"]["items"][i]["name"].upper()
                    if song in name_song:
                        flag = 1
                        webbrowser.open(result["tracks"]["items"][i]["uri"])
                        sleep(5)
                        pyautogui.press("enter")

            if flag == 0:
                song= song.replace(" ", "%20")
                webbrowser.open(f'spotify:search:{song}')
                sleep(3)
                for i in range(4):
                    pyautogui.press("tab")  
                pyautogui.press("enter")

            continue



        elif 'abre' in pedido:

            for apps in programas:
                if apps in pedido:


                    pedido = pedido.replace('abre', '')
                    hablar(f"Abriendo {pedido}")
                    os.system(programas[pedido])

            continue



        #elif '' in pedido:
            




        













pedir_cosas()