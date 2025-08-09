#!/usr/bin/env python3
"""
Standalone test script for the summarize_text function
"""

import re

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

def test_summarize_text():
    """Test the summarize_text function with various inputs"""
    
    print("Testing summarize_text function...\n")
    
    # Test 1: Short text (should return as is)
    short_text = "This is a short text."
    print("Test 1 - Short text:")
    print(f"Input: {short_text}")
    result = summarize_text(short_text)
    print(f"Output: {result}")
    print(f"Length: {len(result)}")
    print("-" * 50)
    
    # Test 2: Long text (should be summarized)
    long_text = """
    Artificial intelligence has made remarkable progress in recent years. 
    Machine learning algorithms have become increasingly sophisticated, 
    enabling computers to perform tasks that were once thought impossible. 
    From natural language processing to computer vision, AI systems are 
    transforming industries across the globe. Researchers continue to push 
    the boundaries of what's possible, developing new techniques and 
    improving existing models. The future of AI looks promising as we 
    discover new applications and capabilities.
    """
    print("Test 2 - Long text:")
    print(f"Input length: {len(long_text.strip())}")
    result = summarize_text(long_text)
    print(f"Output: {result}")
    print(f"Length: {len(result)}")
    print("-" * 50)
    
    # Test 3: Very long text with custom max_length
    very_long_text = """
    Climate change is one of the most pressing challenges facing humanity today. 
    The scientific consensus is clear: human activities, particularly the burning 
    of fossil fuels, are driving unprecedented changes in our planet's climate. 
    Rising global temperatures are causing sea levels to rise, extreme weather 
    events to become more frequent and intense, and ecosystems to shift in ways 
    that threaten biodiversity. However, there is also reason for hope. 
    Renewable energy technologies have advanced rapidly, becoming more efficient 
    and cost-effective than ever before. Solar and wind power are now competitive 
    with fossil fuels in many markets. Electric vehicles are becoming mainstream, 
    and battery technology continues to improve. Governments around the world 
    are implementing policies to reduce greenhouse gas emissions, and many 
    companies are committing to carbon neutrality. International cooperation 
    through agreements like the Paris Climate Accord shows that humanity can 
    work together to address global challenges. While the task ahead is daunting, 
    the tools and knowledge we need to solve this crisis are within our reach.
    """
    print("Test 3 - Very long text with custom max_length (100):")
    print(f"Input length: {len(very_long_text.strip())}")
    result = summarize_text(very_long_text, max_length=100)
    print(f"Output: {result}")
    print(f"Length: {len(result)}")
    print("-" * 50)
    
    # Test 4: Empty text
    empty_text = ""
    print("Test 4 - Empty text:")
    print(f"Input: '{empty_text}'")
    result = summarize_text(empty_text)
    print(f"Output: {result}")
    print("-" * 50)
    
    # Test 5: Text with extra whitespace
    whitespace_text = "   This   text   has   lots   of   spaces.   "
    print("Test 5 - Text with extra whitespace:")
    print(f"Input: '{whitespace_text}'")
    result = summarize_text(whitespace_text)
    print(f"Output: '{result}'")
    print(f"Length: {len(result)}")
    print("-" * 50)
    
    print("All tests completed!")

if __name__ == "__main__":
    test_summarize_text()
