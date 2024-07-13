import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        weather_data = {
            "city": city_name,
            "temperature": main['temp'],
            "pressure": main['pressure'],
            "humidity": main['humidity'],
            "weather": weather['description']
        }
        
        return weather_data
    else:
        print("City not found or API not accessible.")
        return None
