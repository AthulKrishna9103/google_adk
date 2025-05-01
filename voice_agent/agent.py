import asyncio
from google.adk.tools import google_search
from google.adk.agents import LlmAgent
from .util import load_instruction_from_file

voice_agent = LlmAgent(
    name="voice_agent",
    model="gemini-2.0-flash-exp",
    description="A voice agent that can answer questions and perform tasks using voice commands and summarize it.",
    tools=[google_search],
)

root_agent = voice_agent

async def main():
    instruction = load_instruction_from_file("instructions.txt")
    response = await root_agent.run(instruction)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())