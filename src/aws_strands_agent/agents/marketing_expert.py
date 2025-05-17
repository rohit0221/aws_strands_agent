from strands import Agent
from strands.models.litellm import LiteLLMModel
from dotenv import load_dotenv
import os

load_dotenv()

MARKETING_PROMPT = """
You are a senior marketing strategist. Based on provided business insights or product context,
develop focused marketing strategies, including key messaging, channel mix, and campaign ideas.
Be creative but grounded in market logic.
"""

model = LiteLLMModel(
    model_id=os.getenv("MODEL"),  # e.g., "gpt-4o"
    api_key=os.getenv("OPENAI_API_KEY"),
)

agent = Agent(
    model=model,
    system_prompt=MARKETING_PROMPT,
)

if __name__ == "__main__":
    prompt = "Draft a go-to-market strategy for a new AI-powered health tracker wearable."
    response = agent(prompt)
    print(response)
