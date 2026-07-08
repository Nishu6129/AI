from dotenv load_dotenv
from agents import Agent, Runner 
from agents import WebSearchTool, function_tool
import requests

load_dotenv()

@function_tool
def get_weather(city:str):
    """
    Get the current weather for a given city using the WeatherAPI.
    Args:
        city (str): The name of the city to get the weather for.
    Returns:
        str: A string describing the current weather in the specified city.
    """
    url = f"http://api.weatherapi.com/v1/current.json?key=your_weather_api_key&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"The current temperature in {city} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."

#Define agent
hello_agent = Agent(
    name="HelloAgent",
    description="An agent that greets the user and provides a simple response.",
    instructions="You are a friendly assistant that greets the user and provides a simple response.",
    tools=[
        WebSearchTool()
        get_weather
    ]
)


result = Runner.run_agent(hello_agent, input="Hello, how are you?What is the temperature of New Delhi?")


