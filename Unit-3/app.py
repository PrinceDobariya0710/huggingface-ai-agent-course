from smolagents import CodeAgent, HfApiModel
from retriever import load_guest_dataset
from tools import WeatherInfoTool, HubStatsTool
from smolagents import LiteLLMModel
from dotenv import load_dotenv
import os
from smolagents import DuckDuckGoSearchTool

load_dotenv()

# Replace all calls to HfApiModel
model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash",  # you can see other model names here: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models. It is important to prefix the name with "gemini/"
    api_key=os.getenv("GEMINI_API_KEY"),
    max_tokens=8192,
)

# Initialize the web search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the weather tool
weather_info_tool = WeatherInfoTool()

# Initialize the Hub stats tool
hub_stats_tool = HubStatsTool()

# Load the guest dataset and initialize the guest info tool
guest_info_tool = load_guest_dataset()

# Create Alfred with all the tools
alfred = CodeAgent(
    tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool],
    model=model,
    add_base_tools=True,  # Add any additional base tools
    planning_interval=3,  # Enable planning every 3 steps
)
query = "I need to speak with Dr. Nikola Tesla about recent advancements in wireless energy. Can you help me prepare for this conversation?"
response = alfred.run(query)

print("🎩 Alfred's Response:")
print(response)

# alfred_with_memory = CodeAgent(
#     tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool],
#     model=model,
#     add_base_tools=True,
#     planning_interval=3
# )
# # First interaction
# response1 = alfred_with_memory.run("Tell me about Lady Ada Lovelace.")
# print("🎩 Alfred's First Response:")
# print(response1)

# # Second interaction (referencing the first)
# response2 = alfred_with_memory.run(
#     "What projects is she currently working on?", reset=False
# )
# print("🎩 Alfred's Second Response:")
# print(response2)
