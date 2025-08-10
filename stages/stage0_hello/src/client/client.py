from fastmcp import Client
from google.genai.live import asyncio

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY="GEMINI_API_KEY"

gemini_client = genai.Client(api_key=os.getenv(GEMINI_API_KEY))

async def run_client():
    async with Client("http://localhost:4200/dice") as mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents="Refine macrodata of 42",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[mcp_client.session]
            )
        )

        print(response.text)


def main():
    """
    CLI entry point for the MCP client.
    This is synchronous so pyproject's [project.scripts] can call it
    """
    asyncio.run(run_client())

if __name__=="__main__":
    main()
