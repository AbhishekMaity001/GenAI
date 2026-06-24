from asyncio import transports
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location)->str:
    """Get the weather of the given locaiton."""
    return "It's always raining in California"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")