from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import asyncio, os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],  # ensure correct absolute path
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  # ensure the server is running here!
                "transport": "streamable_http"
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-20b")
    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3+5) x 12?"}]}
    )
    print(f"MATH RESPONSE: {math_response['messages'][-1].content}")

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
    )
    print(f"WEATHER RESPONSE: {weather_response['messages'][-1].content}")

asyncio.run(main())