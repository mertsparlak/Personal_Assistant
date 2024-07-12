import speech_recognition as sr
import os
import keyboard
import subprocess
import google.generativeai as genai
import Api_Key as api
import pyttsx3

def speak(text):
    engine = pyttsx3.init() 
    engine.setProperty('rate', 130) # sesin hızını buradan ayarlayabilirsiniz.
    engine.say(text)  # Metni sesli şekilde söyle
    engine.runAndWait()  

# Ses tanımayı başlatıyor
r = sr.Recognizer()

# Sohbet geçmişini saklamak için bir liste oluşturuyoruz
sohbet_gecmisi = []

def sohbet_ekle(mesaj):
    sohbet_gecmisi.append(mesaj)
    if len(sohbet_gecmisi) > 5:  # Gereksiz uzunluktaki geçmişi sınırlandırmak için
        sohbet_gecmisi.pop(0)

def sohbeti_getir():
    return "\n".join(sohbet_gecmisi)

def gemini_ile_konusma(soru):
    sohbet_ekle(f"Kullanıcı: {soru}")
    tam_mesaj = sohbeti_getir() + f"\nKullanıcı: {soru}"
    # Gemini API çağrısı yapılıyor
    genai.configure(api_key=api.Key)
    model = genai.GenerativeModel("models/gemini-pro")
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    response = model.generate_content(tam_mesaj)
    sohbet_ekle(response.text)
    return response.text

with sr.Microphone() as source:
    try:
        while True:
            print("Merhaba, Sizi dinlemeye hazırım.")
            
            # Dinlemeyi başlatmak için basmanız gereken tuşlar (değiştirebilirsiniz dilediğinizce.)
            keyboard.wait("ctrl+alt+m")

            print("Dinliyorum...")
            audio_data = r.listen(source, phrase_time_limit=7) # kaç saniye dinleyeceğini değiştirebilirsiniz burada
            print("İsteğinizi tanımlıyorum...")

            text = r.recognize_google(audio_data)
            print(f"You said {text}")
            speak(f"You said {text}")
            
            if "open notepad" in text.lower():
                subprocess.Popen(r"C:\Windows\System32\notepad.exe")
                print("Senin için note defterini açtım.")
                
            elif "search google for" in text.lower():
                query=text.lower().split("search google for ")[1] #neyi aratmasını söylediysek, split ile search google for kısmını atıyoruz komutumuzdan.
                query=query.replace(" ","+")
                os.system(f"start https://google.com/search?q={query}")
                
            elif "good nigth computer" in text.lower():
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
            
            elif "computer" in text.lower():
                query = text.lower().split("computer ", 1)[1]  # Sadece 'computer ' kelimesinden sonraki kısmı al
                response = gemini_ile_konusma(query)
                print(response)
                speak(response)
   
    except sr.UnknownValueError:
        print("Komutunuzu tanımlayamadım.")
        
        
