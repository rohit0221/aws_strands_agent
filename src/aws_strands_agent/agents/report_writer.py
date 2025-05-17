from strands import Agent
from strands.models.litellm import LiteLLMModel
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

def get_report_writer():
    # Create the model using LiteLLM + OpenAI
    model = LiteLLMModel(
        model_id=os.getenv("MODEL"),  # e.g., "gpt-4o-mini"
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Create the agent using OpenAI (not Bedrock)
    return Agent(
        model=model,
        system_prompt="You are a professional report writer. Write concise, structured summaries.",
    )

if __name__ == "__main__":
    agent = get_report_writer()
    response = agent("Summarize key trends in the global semiconductor industry.")
    print(response)
