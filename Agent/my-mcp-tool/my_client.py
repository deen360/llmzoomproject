#from fastmcp import Client
#
#async def main():
#    async with Client(<TODO>) as mcp_client:
#        # TODO


import asyncio
from fastmcp import Client

client = Client("weather_server.py")

async def call_tool(a: int, b: int) -> int:
    async with client:
        result = await client.call_tool("add", {"a":a,"b":b})
        print(result)



async def weather(city: str) -> float:
    async with Client("weather_server.py") as mcp_client:
        return print(await mcp_client.call_tool("get_weather", {"city": city}))
        # ...


async def main():
    async with Client("weather_server.py") as mcp_client:
        tools = await mcp_client.list_tools()
        return tools



if __name__ == "__main__":
    #test = asyncio.run(weather("berlin"))
    #asyncio.run(call_tool(10, 200))
    tools = asyncio.run(main())

    for tool in tools:
        print(f"Tool: {tool.name}")
        #print(f"Description: {tool.description}")