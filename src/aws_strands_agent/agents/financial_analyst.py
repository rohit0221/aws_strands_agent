from strands import Agent
from strands.models.litellm import LiteLLMModel
from dotenv import load_dotenv
import os

from aws_strands_agent.tools.calculator import calculator

load_dotenv()

FINANCIAL_ANALYST_PROMPT = """
You are a financial analyst. Your role is to analyze financial data and extract insights.
Use the calculator tool when math is needed. Be concise and precise in your response.
"""

model = LiteLLMModel(
    model_id=os.getenv("MODEL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# ✅ Export this agent via a callable function
def financial_analyst(query: str) -> str:
    agent = Agent(
        model=model,
        system_prompt=FINANCIAL_ANALYST_PROMPT,
        tools=[calculator],
    )
    return str(agent(query))


# Optional CLI test
if __name__ == "__main__":
    prompt = "If revenue grew from $1.2M in Q1 to $1.5M in Q2, what is the growth rate?"
    print(financial_analyst(prompt))
