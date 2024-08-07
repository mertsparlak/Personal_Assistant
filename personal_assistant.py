import json
from logging import root
import speech_recognition as sr
import os
import keyboard
import subprocess
import locale
import yfinance as yf
import cryptocompare
import requests
import finance as fin
import api_keys as api
import pyttsx3
import weatherinfo as wi
import gemini_ai as ai



try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'C')

import tkinter as tk
from tkinter import Entry, ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *


def speak(text):
    engine = pyttsx3.init() 
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()

# Ses tanımayı başlatıyor
r = sr.Recognizer()

def start_assistant():
    speak("How can I help you?")
    cryptos = fin.get_crypto_symbols()
    with sr.Microphone() as source:
        try:
            while True:
                print("Dinliyorum...")
                speak("listening...")
                audio_data = r.listen(source, phrase_time_limit=5) # kaç saniye dinleyeceğini değiştirebilirsiniz burada
                print("İsteğinizi tanımlıyorum...")

                text = r.recognize_google(audio_data)
                print(f"You said {text}")
                speak(f"You said {text}")
                
                if "open notepad" in text.lower():
                    subprocess.Popen(r"C:\Windows\System32\notepad.exe")
                    speak("Senin için not defterini açtım.")
                    
                elif "search google for" in text.lower():
                    query=text.lower().split("search google for ")[1] #neyi aratmasını söylediysek, split ile search google for kısmını atıyoruz komutumuzdan.
                    query=query.replace(" ","+")
                    os.system(f"start https://google.com/search?q={query}")
                    
                elif "good night computer" in text.lower():
                    os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
                
                elif "start music" in text.lower():
                    speak("starting music")
                    exec(open(r"open_and_play.py").read())
                    
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

                elif "stock price of" in text.lower():
                    stock_name = text.lower().split("stock price of ")[1]
                    if stock_name in fin.stock_symbols:
                        stock_price = fin.get_stock_price(fin.stock_symbols[stock_name])
                        speak(f"{stock_name.capitalize()} stock price is {stock_price} dollars.")
                        print(f"{stock_name.capitalize()} stock price is {stock_price} dollars.")
                    else:
                        speak("Stock not found.")

                elif "price of" in text.lower():
                    crypto_name = text.lower().split("price of ")[1]
                    if crypto_name in cryptos:
                        crypto_price = fin.get_crypto_price(cryptos[crypto_name])
                        print(f"{crypto_name.capitalize()} price is {crypto_price} dollars")
                        speak(f"{crypto_name.capitalize()} price is {crypto_price} dollars")
                    else:
                        speak("Cryptocurrency not found")
                        
                elif "computer" in text.lower():
                    query = text.lower().split("computer ", 1)[1]
                    response = ai.gemini_ile_konusma(query)
                    print(response)
                    speak(response)
    
        except sr.UnknownValueError:
            print("Komutunuzu tanımlayamadım.")

app = tb.Window(themename="flatly")
app.title("Personal Assistant")
app.geometry("600x450")
app.resizable(False, False)

# Çerçeve (frame) oluşturma
frame = ttk.Frame(app, padding="68")
frame.pack(fill='both', expand=True)

# Başlık etiketi
title_label = ttk.Label(frame, text="Personal Assistant", font=("Helvetica", 20))
title_label.pack(pady=10)

# Açıklama etiketi
desc_label = ttk.Label(frame, text="How can I assist you today?", font=("Helvetica", 14))
desc_label.pack(pady=15)

# Başlat düğmesi
start_button = ttk.Button(frame, text="Start Assistant", command=start_assistant, bootstyle=SUCCESS)
start_button.pack(pady=20)

# Çıkış düğmesi
exit_button = ttk.Button(frame, text="Exit", command=app.quit, bootstyle=DANGER)
exit_button.pack(pady=10)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))

start_button.config(width=15, padding=(10,))
exit_button.config(width=10, )

# Ana döngüyü başlat
app.mainloop()
