from strands import tool
from aws_strands_agent.tools.web_scraper import web_scraper

@tool
def research_specialist(query: str) -> str:
    """
    Simple wrapper around the Tavily-based web scraper.
    """
    return web_scraper(query)
