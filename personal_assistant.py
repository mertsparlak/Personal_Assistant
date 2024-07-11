import speech_recognition as sr
import os
import keyboard
import subprocess

# Ses tanımayı başlatıyor
r = sr.Recognizer()

with sr.Microphone() as source:
    try:
        while True:
            print("Merhaba, Sizi dinlemeye hazırım.")
            
            # Dinlemeyi başlatmak için basmanız gereken tuşlar (değiştirebilirsiniz dilediğinizce.)
            keyboard.wait("ctrl+alt+m")

            print("Dinliyorum...")
            audio_data = r.listen(source, phrase_time_limit=5)
            print("İsteğinizi tanımlıyorum...")

            text = r.recognize_google(audio_data)
            print(f"You said {text}")
            if "open notepad" in text.lower():
                subprocess.Popen(r"C:\Windows\System32\notepad.exe")
                print("Senin için note defterini açtım.")
            elif "search google for" in text.lower():
                query=text.lower().split("search google for ")[1] #neyi aratmasını söylediysek, split ile search google for kısmını atıyoruz komutumuzdan.
                query=query.replace(" ","+")
                os.system(f"start https://google.com/search?q={query}")
            elif "good nigth computer" in text.lower():
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
   
    except sr.UnknownValueError:
        print("Komutunuzu tanımlayamadım.")
        
