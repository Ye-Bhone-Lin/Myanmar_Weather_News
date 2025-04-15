from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
import warnings
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langgraph.prebuilt import create_react_agent

load_dotenv()

class MyanmarNews:
    
    @classmethod
    def get_news(cls, user_input:str):
    
        model = ChatGroq(model_name= "deepseek-r1-distill-llama-70b")
        @tool
        def duckduckgo_search(query: str) -> str:
            """Search Latest Weather News in Myanmar in DuckDuckGo and return including Location"""
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                return DuckDuckGoSearchRun(query=query, source="news").invoke(query)

        @tool
        def weather_search(city: str, country: str) -> str:
            """Retrieve the weather information for a specific city and country"""
            weather_search = OpenWeatherMapAPIWrapper()
            return weather_search.run(f"{city}, {country}")

        tools = [duckduckgo_search, weather_search]
        
        #model_with_tools = model.bind_tools(tools)

        system_prompt = """Act as a Announcer.
        Use the tools at your disposal to perform tasks as needed.
            -duckduckgo_search: use this tool for CURRENT NEWS in Myanmar including LOCATION and MAGNITUDE.
            -weather_search: use this tool for CURRENT WEATHER and FORECAST in Myanmar. 
        if you do not know the answer, try to indicate the weather and news in Myanmar.
        """
        
        agent = create_react_agent(model=model, tools=tools, state_modifier= system_prompt)
        result =  agent.invoke({"messages": [('user',user_input)]})
        return result['messages'][-1].content

