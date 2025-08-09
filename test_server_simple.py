#!/usr/bin/env python3
"""
Simple test to verify the MCP server can start
"""

import subprocess
import sys
import time

def test_server_startup():
    """Test if the server can start without errors"""
    print("Testing MCP server startup...")
    
    try:
        # Start the server process
        process = subprocess.Popen(
            [sys.executable, "server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            text=True
        )
        
        # Give it a moment to start
        time.sleep(2)
        
        # Check if process is still running
        if process.poll() is None:
            print("✅ Server started successfully!")
            print("The server is running and ready to accept MCP connections.")
            
            # Terminate the process
            process.terminate()
            process.wait()
            print("Server terminated.")
        else:
            # Process ended, check for errors
            stdout, stderr = process.communicate()
            print("❌ Server failed to start:")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            
    except Exception as e:
        print(f"❌ Error testing server: {e}")

if __name__ == "__main__":
    test_server_startup()
