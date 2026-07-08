from dotenv load_dotenv
from agents import Agent, Runner 

load_dotenv()

#Define agent
hello_agent = Agent(
    name="HelloAgent",
    description="An agent that greets the user and provides a simple response.",
    instructions="You are a friendly assistant that greets the user and provides a simple response.",
)


result = Runner.run_agent(hello_agent, input="Hello, how are you?")

