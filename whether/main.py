from flask import Flask, render_template
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key_here'
# Replace 'your_city' with the city you want to get weather data for
CITY = 'your_city'

@app.route('/')
def index():
    # Fetch weather data from OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Parse relevant weather information
    weather = {
        'city': CITY,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    # Render HTML template with weather information
    return render_template('weather.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
