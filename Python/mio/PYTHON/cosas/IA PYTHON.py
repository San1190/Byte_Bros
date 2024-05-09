import webbrowser
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hola , soy tu asistente por voz:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Has dicho : {}".format(text))
        print(text)
        if "Amazon" in text:
            webbrowser.open("https://amazon.es")
        if "Noticias" in text:
            webbrowser.open("https://www.elmundo.es/")
    except:
        print('No te he entendido')
