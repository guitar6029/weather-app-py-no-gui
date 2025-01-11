🌦️ Weather App


Welcome to the Weather App! This simple Python-based application fetches weather information for any city and provides the current temperature in either Celsius or Fahrenheit.

🚀 Technologies Used
Python: The core language for the project.

Requests: To fetch data from the Weather API.

python-dotenv: To securely manage environment variables.

📦 Setup
Clone the repository:


sh
```
git clone https://github.com/yourusername/weather-app.git
```
Navigate to the project directory:

sh
```
cd weather-app
```
Create and activate a virtual environment:

sh
```
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```
Install dependencies:

sh
```
pip install requests python-dotenv
```
Create a .env file and add your Weather API key:

env
```
WEATHER_API_KEY=your_api_key_here
```
Run the app:

sh
```
python weather.py
📖 Usage
```
Enter the city name and temperature unit (C for Celsius or F for Fahrenheit):

sh
```
Example: Miami F
```
Get the weather information:

sh
```
The temperature in Miami is 75 degrees Fahrenheit
```
Feel free to explore and enjoy the weather updates! 🌤️
