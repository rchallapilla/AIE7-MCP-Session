# MCP Setup Guide for Cursor

## ✅ Prerequisites Completed
- ✅ uv installed and working
- ✅ Python 3.13+ available
- ✅ All dependencies installed
- ✅ Tavily API key configured
- ✅ MCP server tested and working

## 🚀 Final Steps to Integrate with Cursor

### Step 1: Open MCP Settings in Cursor
1. Open Cursor
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open Command Palette
3. Type "View: Open MCP Settings"
4. Select this option

### Step 2: Configure MCP Server
Replace the contents of the MCP settings with:

```json
{
    "mcpServers": {
        "mcp-server": {
            "command": "uv",
            "args": ["--directory", "C:\\Users\\chrag\\Documents\\AIE7-MCP-Session", "run", "server.py"]
        }
    }
}
```

### Step 3: Restart Cursor
1. Close Cursor completely
2. Reopen Cursor
3. The MCP server should automatically start

### Step 4: Test Your MCP Tools
Once Cursor restarts, you can use these tools:

#### 🔍 Web Search Tool
```
web_search("latest news about artificial intelligence")
```

#### 🎲 Dice Roller Tool
```
roll_dice("3d6", 2)
roll_dice("1d20")
```

#### 📝 Text Summarizer Tool
```
summarize_text("Your long text here", 150)
```

## 🛠️ Available Tools

### 1. web_search(query: str)
- **Purpose**: Search the web for information
- **Example**: `web_search("Boston weather today")`
- **Returns**: Search results from Tavily API

### 2. roll_dice(notation: str, num_rolls: int = 1)
- **Purpose**: Roll dice using D&D notation
- **Examples**: 
  - `roll_dice("3d6")` - Roll 3 six-sided dice
  - `roll_dice("1d20", 5)` - Roll 1 twenty-sided die 5 times
- **Returns**: Dice roll results

### 3. summarize_text(text: str, max_length: int = 200)
- **Purpose**: Summarize text to specified length
- **Example**: `summarize_text("Long article text...", 100)`
- **Returns**: Summarized text

## 🔧 Troubleshooting

### If MCP doesn't work:
1. Check that uv is in your PATH
2. Verify the path in the config matches your actual directory
3. Check that the .env file contains your Tavily API key
4. Restart Cursor

### To verify MCP is working:
1. Open Cursor
2. Try using one of the tools in a chat
3. You should see the tool being called and results returned

## 📁 Files Created
- `mcp-config.json` - MCP configuration file
- `MCP_SETUP_GUIDE.md` - This guide

Your MCP server is ready to use! 🎉
