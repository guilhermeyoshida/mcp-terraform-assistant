import argparse
import logging
from typing import Optional

from .config import Config
from .server import FastMCP

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="MCP server for Terraform operations")
    parser.add_argument("--host", default="localhost", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8080, help="Port to bind to")
    parser.add_argument("--terraform-dir", default=".", help="Directory containing Terraform files")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()

def main() -> None:
    """Main entry point for the MCP server."""
    args = parse_args()
    config = Config.from_args(args)
    
    # Initialize FastMCP server
    server = FastMCP("terraform-assistant")
    
    # Start the server
    server.start() 