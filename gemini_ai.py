import google.generativeai as genai
import api_keys as api

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
    genai.configure(api_key=api.gemini_api_key)
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