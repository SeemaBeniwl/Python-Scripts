# Flask Weather App

A beautiful Flask web application that allows users to search for any city and view current weather conditions with weather icons.

## Features

- 🌍 **City Search** - Enter any city name to get weather info
- 🌡️ **Current Temperature** - See real-time temperature and "feels like" temperature
- 💧 **Humidity & Pressure** - Get detailed atmospheric data
- 💨 **Wind Speed** - Check wind conditions
- 🎨 **Beautiful UI** - Responsive, modern design with weather emojis
- 🔍 **Error Handling** - Helpful error messages for invalid cities
- 📱 **Mobile Friendly** - Works perfectly on all devices

## Installation

### 1. Clone or Download the Project
```bash
cd weather-app
```

### 2. Create Virtual Environment (Already Done)
A virtual environment has been created at `.venv`

### 3. Install Dependencies (Already Done)
All dependencies have been installed:
- Flask 2.3.0
- Requests 2.31.0
- Python-dotenv 1.0.0

### 4. Get OpenWeatherMap API Key
1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to your API keys page
4. Copy your API key (the default one is fine)

### 5. Create .env File
```bash
# Copy .env.example to .env
copy .env.example .env
```

Then edit `.env` and replace `your_api_key_here` with your actual API key:
```
OPENWEATHER_API_KEY=your_actual_api_key_here
```

## Running the App

### On Windows:
```bash
# Navigate to the weather-app directory
cd weather-app

# Run the app with your configured Python environment
"c:/Users/seema/Documents/Python Scripts/.venv/Scripts/python.exe" app.py
```

### Or using Python directly:
```bash
python app.py
```

The app will start on `http://localhost:5000`

## Usage

1. Open your browser and go to `http://localhost:5000`
2. Enter a city name (e.g., "London", "New York", "Tokyo")
3. Click "Search Weather"
4. View the current weather with:
   - Temperature in Celsius
   - Weather condition with emoji icon
   - Humidity percentage
   - Wind speed
   - Atmospheric pressure
   - "Feels like" temperature

## Project Structure

```
weather-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (NOT in git)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore patterns
├── README.md             # This file
├── static/
│   └── css/
│       └── style.css     # Application styling
└── templates/
    ├── base.html         # Base HTML template
    ├── index.html        # Home page with search form
    └── weather.html      # Weather results page
```

## API Information

This app uses the **OpenWeatherMap Current Weather Data API**:
- Endpoint: `https://api.openweathermap.org/data/2.5/weather`
- Free tier available with limitations
- No credit card required for free tier

## Weather Icons

The app displays weather conditions using Unicode emojis:
- ☀️ Clear sky (day)
- 🌙 Clear sky (night)
- ⛅ Partly cloudy
- ☁️ Cloudy/Overcast
- 🌧️ Rain
- ⛈️ Thunderstorm
- ❄️ Snow
- 🌫️ Mist/Fog

## Error Handling

The app gracefully handles:
- Cities that don't exist → "City not found" message
- API errors → "Unable to fetch weather data" message
- Empty search → "Please enter a city name" message
- Network issues → Appropriate error messages

## Future Enhancements

- [ ] 5-day weather forecast
- [ ] Multiple city comparison
- [ ] Geolocation-based weather
- [ ] Temperature unit toggle (Celsius/Fahrenheit)
- [ ] Search history
- [ ] Weather alerts
- [ ] Dark mode
- [ ] City suggestions (autocomplete)

## Troubleshooting

### "API key not found" error
- Make sure you created a `.env` file
- Verify your API key is correctly copied
- Restart the Flask app after creating `.env`

### "City not found" error
- Check the spelling of the city name
- Try using the full city name with country code (e.g., "London, UK")

### App won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.8 or higher
- Check if port 5000 is already in use

## Security Notes

- Never commit `.env` file to git (it's in `.gitignore`)
- Always store API keys in environment variables
- Never hardcode API keys in your code

## License

Free to use for personal projects.

## Support

For API issues, visit [OpenWeatherMap Documentation](https://openweathermap.org/weather-conditions)

---

**Made with ❤️ using Flask**
