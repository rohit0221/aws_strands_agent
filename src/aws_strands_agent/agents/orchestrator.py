from strands import Agent
from strands.models.litellm import LiteLLMModel
from aws_strands_agent.agents.research_specialist import research_specialist
from aws_strands_agent.agents.report_writer import get_report_writer

import os
from dotenv import load_dotenv
load_dotenv()

# Prompt
ORCHESTRATOR_PROMPT = """
You are a strategy orchestrator. You will delegate research tasks to a research specialist.
After receiving insights, summarize them for strategic decision-making using the report writer.
"""

# Model config
model = LiteLLMModel(
    model_id="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Agent with research tool
orchestrator = Agent(
    model=model,
    system_prompt=ORCHESTRATOR_PROMPT,
    tools=[research_specialist]
)

# Run task
query = "What are the latest developments in generative AI for healthcare in 2025?"
raw_insights = orchestrator(query)

# Use report_writer to polish
report_writer = get_report_writer()
final_summary = report_writer(f"Polish and summarize:\n\n{raw_insights}")

print("\n🔍 Raw Insight:\n", raw_insights)
print("\n📝 Final Summary:\n", final_summary)
