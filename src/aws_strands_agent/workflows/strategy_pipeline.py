from aws_strands_agent.agents.research_specialist import research_specialist
from aws_strands_agent.agents.financial_analyst import financial_analyst 
from aws_strands_agent.agents.marketing_expert import agent as marketing_agent
from aws_strands_agent.agents.report_writer import get_report_writer

def run_strategy_pipeline(query: str) -> str:
    print("🔍 Step 1: Research Specialist")
    research = research_specialist(query)
    print("✅ Research Output:\n", research, "\n")

    print("💹 Step 2: Financial Analyst")
    finance = financial_analyst(query)
    print("✅ Financial Insights:\n", finance, "\n")

    print("📢 Step 3: Marketing Expert")
    marketing = marketing_agent(f"Based on this context: {research}\n\n{query}")
    print("✅ Marketing Strategy:\n", marketing, "\n")

    # Combine everything for final summary
    combined_context = f"""
== RESEARCH INSIGHTS ==
{research}

== FINANCIAL INSIGHTS ==
{finance}

== MARKETING STRATEGY ==
{marketing}
"""

    print("📝 Step 4: Report Writer")
    report_writer = get_report_writer()
    final_summary = report_writer(f"Summarize this into a 1-page executive strategy report:\n\n{combined_context}")
    return final_summary

if __name__ == "__main__":
    strategic_query = "What is the market outlook and go-to-market plan for AI-powered health wearables in 2025?"
    summary = run_strategy_pipeline(strategic_query)
    print("\n📌 FINAL STRATEGY SUMMARY:\n", summary)
