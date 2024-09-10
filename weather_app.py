import requests

# Replace with your own OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city_name):
    # Construct the final URL with the city name and API key
    request_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    
    # Send the request to OpenWeatherMap API
    response = requests.get(request_url)
    
    # Parse the JSON response
    data = response.json()
    
    # Check if the city is found
    if data['cod'] == 200:
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']
        
        # Display weather data
        temperature = main['temp']
        humidity = main['humidity']
        wind_speed = wind['speed']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found. Please check the name and try again.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
