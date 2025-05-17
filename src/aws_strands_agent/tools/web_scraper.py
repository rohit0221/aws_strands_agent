from strands import tool
import requests
import os

@tool
def web_scraper(query: str) -> str:
    """Search the web using Tavily and return a concise summary."""
    api_key = os.getenv("TAVILY_API_KEY")
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic",
        "include_answer": True,
        "include_raw_content": False,
        "include_images": False,
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json().get("answer", "No answer found.")
    except Exception as e:
        return f"Error from Tavily: {str(e)}"
