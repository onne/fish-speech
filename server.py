#!/usr/bin/env python3
"""
Fish Speech TTS Server Wrapper
Simplified server for Interactive Reader integration
"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(__file__))

# Import and run the API server
from tools.api_server import API
import uvicorn
import re

if __name__ == "__main__":
    # Initialize with default settings optimized for macOS
    api = API()
    
    # Override args for macOS
    api.args.device = "mps" if os.system("sysctl -n machdep.cpu.brand_string | grep -q 'Apple'") == 0 else "cpu"
    api.args.listen = "0.0.0.0:8883"
    api.args.workers = 1
    
    # Parse listen address
    match = re.search(r"\[([^\]]+)\]:(\d+)$", api.args.listen)
    if match:
        host, port = match.groups()  # IPv6
    else:
        host, port = api.args.listen.split(":")  # IPv4
    
    print(f"[Fish Speech] Starting server on {host}:{port}")
    print(f"[Fish Speech] Device: {api.args.device}")
    
    uvicorn.run(
        api.app,
        host=host,
        port=int(port),
        workers=api.args.workers,
        log_level="info",
    )
