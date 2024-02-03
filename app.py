import requests

class WeatherChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",  
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_description = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
            else:
                return "Sorry, I couldn't retrieve the weather information at the moment."

        except Exception as e:
            print(e)
            return "An error occurred while fetching the weather information."

def chatbot(user_input):
    if any(greeting in user_input.lower() for greeting in ['hello', 'hi', 'hey']):
        return "Hello! How can I help you today?"
    elif 'weather' in user_input.lower():
        city = input("Please enter the city for weather information: ")
        return weather_bot.get_weather(city)
    elif 'exit' in user_input.lower():
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I didn't understand that. How can I assist you?"

#
weather_api_key = '7154fa330f4aec2162e02885fa4be53d'
weather_bot = WeatherChatbot(api_key=weather_api_key)

if __name__ == "__main__":
    print("This is the Enhanced Weather Chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("User: ")
        response = chatbot(user_input)
        print("Chatbot:", response)

        if 'exit' in user_input.lower():
            break
