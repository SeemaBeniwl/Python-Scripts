# Flask Weather App - Project Plan

## Project Overview
A Flask web application that allows users to enter a city name and displays the current weather with weather icons.

---

## Project Structure
```
weather-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Styling for the application
│   └── images/
│       └── weather-icons/ # Weather condition icons (optional)
└── templates/
    ├── base.html          # Base template with layout
    ├── index.html         # Home page with search form
    └── weather.html       # Weather display page
```

---

## Key Features

### 1. **User Input**
   - Text input field for city name
   - Search button to fetch weather
   - Error handling for invalid/not found cities

### 2. **Weather Display**
   - Current temperature
   - Weather condition (sunny, cloudy, rainy, etc.)
   - Weather icon / emoji representation
   - Additional details:
     - "Feels like" temperature
     - Humidity percentage
     - Wind speed
     - Pressure
     - UV index (optional)

### 3. **User Experience**
   - Clear, responsive UI
   - Weather icons for visual representation
   - Search history (optional)
   - Unit selection (Celsius/Fahrenheit)
   - Error messages for failed searches

---

## Technology Stack

### Backend
- **Flask** - Web framework
- **Requests** - HTTP library for API calls
- **Python 3.8+**

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling
- **Optional: Jinja2** (Flask templating - built-in)

### External API
- **OpenWeatherMap API** (Free tier available)
  - Alternative: WeatherAPI.com, Weather.gov

### Icons
- Weather emoji Unicode characters, OR
- Font Awesome icons, OR
- Open-source weather icon set

---

## API Integration

### OpenWeatherMap API
- Endpoint: `https://api.openweathermap.org/data/2.5/weather`
- Required Parameters:
  - `q` (city name)
  - `appid` (API key)
  - `units` (metric/imperial)

### Response Data
```json
{
  "name": "London",
  "main": {
    "temp": 15.5,
    "feels_like": 14.2,
    "humidity": 72,
    "pressure": 1013
  },
  "weather": [
    {
      "main": "Cloudy",
      "description": "overcast clouds",
      "icon": "04d"
    }
  ],
  "wind": {
    "speed": 4.5
  }
}
```

---

## Implementation Steps

### Phase 1: Setup & Structure
- [ ] Create project directory
- [ ] Set up virtual environment
- [ ] Create `requirements.txt` with dependencies
- [ ] Create basic Flask app with routes
- [ ] Set up folder structure

### Phase 2: Frontend
- [ ] Create base HTML template
- [ ] Create index page with search form
- [ ] Create weather results page
- [ ] Style with CSS (normalize, layout, responsiveness)
- [ ] Add weather icons/emojis

### Phase 3: Backend
- [ ] Set up environment variables for API key
- [ ] Create function to fetch weather data from API
- [ ] Create Flask routes:
  - `GET /` - Home page
  - `POST /search` or `GET /weather?city=...` - Search and display
- [ ] Add error handling (city not found, API errors, etc.)

### Phase 4: Enhancement
- [ ] Add input validation
- [ ] Add search history (cookies or session)
- [ ] Add unit toggle (C/F)
- [ ] Add more weather details
- [ ] Improve responsive design
- [ ] Add loading spinner

### Phase 5: Testing & Deployment
- [ ] Test with various cities
- [ ] Test error scenarios
- [ ] Test mobile responsiveness
- [ ] Consider deployment (Heroku, PythonAnywhere, etc.)

---

## Routes & Views

### Route 1: Home Page
- **URL:** `/`
- **Method:** GET
- **Returns:** HTML form for city search
- **Template:** `index.html`

### Route 2: Weather Search
- **URL:** `/weather` or `/search`
- **Method:** GET/POST
- **Parameters:** city name
- **Returns:** Weather data display or error message
- **Template:** `weather.html`

---

## Dependencies

```txt
Flask==2.3.0
requests==2.31.0
python-dotenv==1.0.0
```

---

## Weather Icon Mapping

Map API icon codes to emoji or Font Awesome icons:
```python
WEATHER_ICONS = {
    '01d': '☀️',   # Clear day
    '01n': '🌙',   # Clear night
    '02d': '⛅',   # Partly cloudy day
    '02n': '🌤️',   # Partly cloudy night
    '03d': '☁️',   # Cloudy
    '04d': '☁️',   # Overcast
    '09d': '🌧️',   # Light rain
    '10d': '🌦️',   # Rain
    '11d': '⛈️',   # Thunderstorm
    '13d': '❄️',   # Snow
    '50d': '🌫️',   # Mist
}
```

---

## Sample Code Structure

### app.py
```python
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST', 'GET'])
def get_weather():
    city = request.args.get('city') or request.form.get('city')
    # Fetch and return weather data
    pass

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Security Considerations
- Store API key in `.env` file (never commit to git)
- Validate user input
- Add rate limiting (optional)
- Use HTTPS in production

---

## Optional Features (Phase 2)
- 5-day forecast
- Multiple city comparison
- Geolocation-based weather
- Weather alerts
- Dark mode
- Chart/graph for temperature trends
