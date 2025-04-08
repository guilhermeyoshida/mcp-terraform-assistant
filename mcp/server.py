import logging
import os
import subprocess
from typing import Dict, Any

from .config import Config

class Server:
    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        if config.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    def start(self):
        """Start the MCP server"""
        self.logger.info(f"Starting MCP server on {self.config.host}:{self.config.port}")
        # TODO: Implement MCP protocol server
        # This will be implemented using the mcp library
        pass

    def run_terraform(self, command: str, args: Dict[str, Any] = None) -> Dict[str, Any]:
        """Run a Terraform command and return the result"""
        if not os.path.exists(self.config.terraform_dir):
            raise FileNotFoundError(f"Terraform directory not found: {self.config.terraform_dir}")

        cmd = ["terraform", command]
        if args:
            for key, value in args.items():
                if value is not None:
                    cmd.extend([f"-{key}", str(value)])

        try:
            result = subprocess.run(
                cmd,
                cwd=self.config.terraform_dir,
                capture_output=True,
                text=True,
                check=True
            )
            return {
                "success": True,
                "output": result.stdout,
                "error": None
            }
        except subprocess.CalledProcessError as e:
            return {
                "success": False,
                "output": e.stdout,
                "error": e.stderr
            } 