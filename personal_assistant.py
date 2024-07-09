import speech_recognition as sr
import os
import keyboard
import subprocess

# Ses tanımayı başlatıyor
r = sr.Recognizer()

with sr.Microphone() as source:
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
