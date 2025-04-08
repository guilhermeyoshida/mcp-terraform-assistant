from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    """Configuration for the MCP server."""
    host: str
    port: int
    terraform_dir: str
    debug: bool

    @classmethod
    def from_args(cls, args) -> "Config":
        """Create a Config instance from command line arguments."""
        return cls(
            host=args.host,
            port=args.port,
            terraform_dir=args.terraform_dir,
            debug=args.debug
        ) 