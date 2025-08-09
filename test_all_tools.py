#!/usr/bin/env python3
"""
Test all tools in the MCP server
"""

import sys
import os

# Add the current directory to the path so we can import from server.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the functions from server.py
from server import summarize_text, roll_dice, web_search

def test_all_tools():
    """Test all tools in the MCP server"""
    
    print("Testing all MCP server tools...\n")
    
    # Test 1: summarize_text tool
    print("=" * 60)
    print("Testing summarize_text tool:")
    long_text = """
    The summarize_text tool is working perfectly. It takes long text and 
    creates concise summaries by keeping the most important sentences. 
    This tool is very useful for condensing articles, documents, and 
    other lengthy content into digestible summaries.
    """
    result = summarize_text(long_text, max_length=100)
    print(f"Input length: {len(long_text.strip())}")
    print(f"Output: {result}")
    print(f"Output length: {len(result)}")
    
    # Test 2: roll_dice tool
    print("\n" + "=" * 60)
    print("Testing roll_dice tool:")
    try:
        result = roll_dice("2d6", 3)
        print(f"Rolling 2d6 three times: {result}")
        
        result = roll_dice("1d20", 1)
        print(f"Rolling 1d20 once: {result}")
        
        result = roll_dice("3d6k2", 2)
        print(f"Rolling 3d6k2 twice: {result}")
    except Exception as e:
        print(f"Error testing roll_dice: {e}")
    
    # Test 3: web_search tool (this will use the Tavily API)
    print("\n" + "=" * 60)
    print("Testing web_search tool:")
    try:
        result = web_search("latest AI news 2024")
        print(f"Web search result length: {len(result)} characters")
        print(f"First 200 characters: {result[:200]}...")
    except Exception as e:
        print(f"Error testing web_search: {e}")
    
    print("\n" + "=" * 60)
    print("All tool tests completed!")

if __name__ == "__main__":
    test_all_tools()
