# Weather App

This is a simple weather application that displays the current weather information for a given location.

## Features

- Enter a city name to retrieve the current weather data
- Displays temperature, weather condition, description, pressure, humidity, and wind speed
- Automatically detects and displays the local time of the selected location
- Uses geolocation to fetch latitude and longitude information
- Provides text-to-speech functionality to announce the weather information
- Changes the logo image based on the weather condition

## Technologies Used

- Python
- Tkinter (GUI library)
- Requests (HTTP library)
- Geopy (geocoding library)
- Timezonefinder (timezone library)
- Win32com (Windows voice library)
- PIL (Python Imaging Library)
- PrettyTable (tabular data formatting)

## How to Use

1. Clone the repository: `git clone https://github.com/Srish0218/weather-app.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `python weather.py`
4. Enter the name of the city you want to retrieve the weather data for and press Enter or click the search button.
5. The application will display the weather information along with the current local time and the corresponding weather logo.

## Screenshots

![Weather App](screenshots/weather_app.png)

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute and make improvements!
