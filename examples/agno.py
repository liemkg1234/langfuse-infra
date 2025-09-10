import asyncio
import os
from textwrap import dedent

import nest_asyncio
from agno.agent import Agent
from agno.models.openai import OpenAILike
from agno.playground import Playground, serve_playground_app
from agno.tools.mcp import MCPTools
from fastapi.middleware.cors import CORSMiddleware
from config import tracer
import openlit


nest_asyncio.apply()


llm = OpenAILike(
    id=os.environ.get("FINHOME_AI_MODEL"),
    api_key=os.environ.get("LLM_LAB_API_KEY"),
    base_url=os.environ.get("LLM_GATEWAY_URL"),
)


async def run_server():
    # Agents
    mcp = MCPTools(url=os.environ.get('MCP_GATEWAY_URL'), transport="streamable-http")
    await mcp.connect()

    agent = Agent(
        name="Custom Agent",
        model=llm,
        tools=[mcp],
        instructions=dedent("""\
            You are a assistant Chatbot
            You always use /no_think
        """),
        add_history_to_messages=True,
        num_history_responses=20,
        show_tool_calls=True,
        debug_mode=True,
    )

    playground = Playground(agents=[agent])
    app = playground.get_app()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://app.agno.com",
            "http://localhost:3001",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    serve_playground_app(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # Enable Tracing
    openlit.init(tracer=tracer._otel_tracer, disable_batch=True)
    asyncio.run(run_server())
