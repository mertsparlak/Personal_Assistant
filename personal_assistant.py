import json
import speech_recognition as sr
import os
import keyboard
import subprocess
import google.generativeai as genai
import api_keys as api
import pyttsx3
import weatherinfo as wi
import gemini_ai as ai


def speak(text):
    engine = pyttsx3.init() 
    engine.setProperty('rate', 130) # sesin hızını buradan ayarlayabilirsiniz.
    engine.say(text)  # Metni sesli şekilde söyle
    engine.runAndWait()  

# Ses tanımayı başlatıyor
r = sr.Recognizer()

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
            
            elif "start music" in text.lower():
                speak("starting music")
                exec(open(r"C:\Users\merts\OneDrive\Belgeler\GitHub\Personal_Assistant\open_and_play.py").read())
                
            elif "pause music" in text.lower() or "pause song" in text.lower() or "play music" in text.lower() or "resume music" in text.lower():

                exec(open(r"C:\Users\merts\OneDrive\Belgeler\GitHub\Personal_Assistant\pause_or_play_music").read())
                
            elif "how is the weather in" in text.lower():
                name_city = text.lower().split("how is the weather in ")[1]
                response = wi.get_weather(city_name=name_city, api_key=api.open_weather_map_api_key)
                if response is not None:
                    weather_data = response
                    response_text = f"For {weather_data['city']}, Weather is {weather_data['weather']}, Temperature is {weather_data['temperature']} celsius, Humidity is {weather_data['humidity']} percent"
                    print(response_text)
                    speak(response_text)
                else:
                    print("Weather data could not be retrieved.")
                    speak("Weather data could not be retrieved.")

                    
            elif "computer" in text.lower():
                query = text.lower().split("computer ", 1)[1]  # Sadece 'computer ' kelimesinden sonraki kısmı al
                response = ai.gemini_ile_konusma(query)
                print(response)
                speak(response)
   
    except sr.UnknownValueError:
        print("Komutunuzu tanımlayamadım.")
        
        
