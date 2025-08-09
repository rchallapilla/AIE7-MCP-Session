from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import os
from dice_roller import DiceRoller
import re

load_dotenv()

mcp = FastMCP("mcp-server")

# Initialize TavilyClient only if API key is available
try:
    from tavily import TavilyClient
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if tavily_api_key:
        client = TavilyClient(tavily_api_key)
        tavily_available = True
    else:
        client = None
        tavily_available = False
except Exception as e:
    client = None
    tavily_available = False

@mcp.tool()
def web_search(query: str) -> str:
    """Search the web for information about the given query"""
    if not tavily_available:
        return "Web search is not available. Please set the TAVILY_API_KEY environment variable."
    try:
        search_results = client.get_search_context(query=query)
        return search_results
    except Exception as e:
        return f"Error performing web search: {str(e)}"

@mcp.tool()
def roll_dice(notation: str, num_rolls: int = 1) -> str:
    """Roll the dice with the given notation"""
    roller = DiceRoller(notation, num_rolls)
    return str(roller)

"""
Add your own tool here, and then use it through Cursor!
"""
@mcp.tool()
def summarize_text(text: str, max_length: int = 200) -> str:
    """Summarize the given text to a specified maximum length"""
    if not text or len(text.strip()) == 0:
        return "No text provided to summarize."
    
    # Clean the text
    cleaned_text = re.sub(r'\s+', ' ', text.strip())
    
    # If text is already shorter than max_length, return as is
    if len(cleaned_text) <= max_length:
        return cleaned_text
    
    # Simple summarization: take first few sentences
    sentences = re.split(r'[.!?]+', cleaned_text)
    summary_parts = []
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        # Add period back to sentence
        sentence_with_period = sentence + "."
        
        if current_length + len(sentence_with_period) <= max_length:
            summary_parts.append(sentence_with_period)
            current_length += len(sentence_with_period)
        else:
            break
    
    if not summary_parts:
        # If no sentences fit, truncate the text
        summary = cleaned_text[:max_length-3] + "..."
    else:
        summary = " ".join(summary_parts)
        if len(summary) < len(cleaned_text):
            summary = summary.rstrip(".") + "..."
    
    return summary


if __name__ == "__main__":
    mcp.run(transport="stdio")