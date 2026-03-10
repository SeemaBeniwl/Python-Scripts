from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Weather emoji mapping
WEATHER_ICONS = {
    '01d': '☀️',      # Clear day
    '01n': '🌙',      # Clear night
    '02d': '⛅',      # Partly cloudy day
    '02n': '🌤️',     # Partly cloudy night
    '03d': '☁️',      # Cloudy day
    '03n': '☁️',      # Cloudy night
    '04d': '☁️',      # Overcast day
    '04n': '☁️',      # Overcast night
    '09d': '🌧️',     # Light rain
    '09n': '🌧️',     # Light rain night
    '10d': '🌦️',     # Rain day
    '10n': '🌧️',     # Rain night
    '11d': '⛈️',      # Thunderstorm day
    '11n': '⛈️',      # Thunderstorm night
    '13d': '❄️',      # Snow day
    '13n': '❄️',      # Snow night
    '50d': '🌫️',     # Mist day
    '50n': '🌫️',     # Mist night
}

@app.route('/')
def index():
    """Render the home page with search form."""
    return render_template('index.html')

@app.route('/weather', methods=['POST', 'GET'])
def get_weather():
    """Fetch and display weather for a given city."""
    try:
        # Get city name from form or query parameters
        city = request.args.get('city') or request.form.get('city')
        
        if not city:
            return render_template('weather.html', error='Please enter a city name.'), 400
        
        # Fetch weather data from API
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use Celsius by default
        }
        
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 404:
            return render_template('weather.html', error=f'City "{city}" not found. Please try again.'), 404
        
        if response.status_code != 200:
            return render_template('weather.html', error='Unable to fetch weather data. Please try again later.'), 500
        
        data = response.json()
        
        # Extract weather information
        weather_info = {
            'city': data['name'],
            'country': data['sys'].get('country', 'N/A'),
            'temperature': round(data['main']['temp'], 1),
            'feels_like': round(data['main']['feels_like'], 1),
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description'].capitalize(),
            'icon': WEATHER_ICONS.get(data['weather'][0]['icon'], '🌡️'),
            'weather_main': data['weather'][0]['main']
        }
        
        return render_template('weather.html', weather=weather_info)
    
    except Exception as e:
        return render_template('weather.html', error=f'An error occurred: {str(e)}'), 500

@app.route('/search', methods=['GET'])
def search():
    """Alternative search route - redirects to weather page."""
    city = request.args.get('city')
    if city:
        return get_weather()
    return index()

if __name__ == '__main__':
    app.run(debug=True)
