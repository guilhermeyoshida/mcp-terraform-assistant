import subprocess
from typing import List

from mcp.server.fastmcp import FastMCP, Tool, ToolCall, ToolCallStatus

# Define the tools for Terraform operations
def get_terraform_tools() -> List[Tool]:
    return [
        Tool(
            name="terraform_init",
            description="Initialize a Terraform working directory",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                    "backend_config": {
                        "type": "object",
                        "description": "Backend configuration for Terraform",
                        "additionalProperties": True,
                    },
                },
                "required": ["working_dir"],
            },
        ),
        Tool(
            name="terraform_plan",
            description="Generate and show an execution plan for Terraform",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                    "var_file": {
                        "type": "string",
                        "description": "Path to a variables file",
                    },
                    "var": {
                        "type": "object",
                        "description": "Variables to set for the Terraform plan",
                        "additionalProperties": True,
                    },
                },
                "required": ["working_dir"],
            },
        ),
        Tool(
            name="terraform_apply",
            description="Apply the changes required to reach the desired state of the configuration",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                    "auto_approve": {
                        "type": "boolean",
                        "description": "Skip interactive approval of plan before applying",
                        "default": False,
                    },
                    "var_file": {
                        "type": "string",
                        "description": "Path to a variables file",
                    },
                    "var": {
                        "type": "object",
                        "description": "Variables to set for the Terraform apply",
                        "additionalProperties": True,
                    },
                },
                "required": ["working_dir"],
            },
        ),
        Tool(
            name="terraform_destroy",
            description="Destroy the infrastructure managed by Terraform",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                    "auto_approve": {
                        "type": "boolean",
                        "description": "Skip interactive approval of plan before destroying",
                        "default": False,
                    },
                    "var_file": {
                        "type": "string",
                        "description": "Path to a variables file",
                    },
                    "var": {
                        "type": "object",
                        "description": "Variables to set for the Terraform destroy",
                        "additionalProperties": True,
                    },
                },
                "required": ["working_dir"],
            },
        ),
        Tool(
            name="terraform_validate",
            description="Validate the syntax and internal consistency of Terraform files",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                },
                "required": ["working_dir"],
            },
        ),
        Tool(
            name="terraform_show",
            description="Show the current state or a saved plan",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                    "plan_file": {
                        "type": "string",
                        "description": "Path to a saved plan file",
                    },
                },
                "required": ["working_dir"],
            },
        ),
        Tool(
            name="terraform_workspace_list",
            description="List Terraform workspaces",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                },
                "required": ["working_dir"],
            },
        ),
        Tool(
            name="terraform_workspace_select",
            description="Select a Terraform workspace",
            parameters={
                "type": "object",
                "properties": {
                    "working_dir": {
                        "type": "string",
                        "description": "Path to the Terraform working directory",
                    },
                    "name": {
                        "type": "string",
                        "description": "Name of the workspace to select",
                    },
                },
                "required": ["working_dir", "name"],
            },
        ),
    ]

# Implement the tool handlers
async def handle_terraform_init(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    backend_config = tool_call.parameters.get("backend_config", {})
    
    cmd = ["terraform", "init"]
    
    # Add backend config if provided
    for key, value in backend_config.items():
        cmd.extend(["-backend-config", f"{key}={value}"])
    
    try:
        result = subprocess.run(
            cmd,
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

async def handle_terraform_plan(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    var_file = tool_call.parameters.get("var_file")
    var = tool_call.parameters.get("var", {})
    
    cmd = ["terraform", "plan"]
    
    # Add var-file if provided
    if var_file:
        cmd.extend(["-var-file", var_file])
    
    # Add vars if provided
    for key, value in var.items():
        cmd.extend(["-var", f"{key}={value}"])
    
    try:
        result = subprocess.run(
            cmd,
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

async def handle_terraform_apply(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    auto_approve = tool_call.parameters.get("auto_approve", False)
    var_file = tool_call.parameters.get("var_file")
    var = tool_call.parameters.get("var", {})
    
    cmd = ["terraform", "apply"]
    
    if auto_approve:
        cmd.append("-auto-approve")
    
    # Add var-file if provided
    if var_file:
        cmd.extend(["-var-file", var_file])
    
    # Add vars if provided
    for key, value in var.items():
        cmd.extend(["-var", f"{key}={value}"])
    
    try:
        result = subprocess.run(
            cmd,
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

async def handle_terraform_destroy(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    auto_approve = tool_call.parameters.get("auto_approve", False)
    var_file = tool_call.parameters.get("var_file")
    var = tool_call.parameters.get("var", {})
    
    cmd = ["terraform", "destroy"]
    
    if auto_approve:
        cmd.append("-auto-approve")
    
    # Add var-file if provided
    if var_file:
        cmd.extend(["-var-file", var_file])
    
    # Add vars if provided
    for key, value in var.items():
        cmd.extend(["-var", f"{key}={value}"])
    
    try:
        result = subprocess.run(
            cmd,
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

async def handle_terraform_validate(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    
    try:
        result = subprocess.run(
            ["terraform", "validate"],
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

async def handle_terraform_show(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    plan_file = tool_call.parameters.get("plan_file")
    
    cmd = ["terraform", "show"]
    
    if plan_file:
        cmd.append(plan_file)
    
    try:
        result = subprocess.run(
            cmd,
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

async def handle_terraform_workspace_list(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    
    try:
        result = subprocess.run(
            ["terraform", "workspace", "list"],
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

async def handle_terraform_workspace_select(tool_call: ToolCall) -> ToolCallStatus:
    working_dir = tool_call.parameters.get("working_dir")
    name = tool_call.parameters.get("name")
    
    try:
        result = subprocess.run(
            ["terraform", "workspace", "select", name],
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return ToolCallStatus(
            status="completed",
            output=result.stdout,
        )
    except subprocess.CalledProcessError as e:
        return ToolCallStatus(
            status="failed",
            output=f"Error: {e.stderr}",
        )

# Create the MCP server
def create_mcp_server() -> FastMCP:
    tools = get_terraform_tools()
    
    # Create the MCP server
    mcp = FastMCP(
        name="terraform-iac-assistant",
        description="An AI assistant for managing infrastructure as code with Terraform",
        tools=tools,
    )
    
    # Register tool handlers
    mcp.register_tool_handler("terraform_init", handle_terraform_init)
    mcp.register_tool_handler("terraform_plan", handle_terraform_plan)
    mcp.register_tool_handler("terraform_apply", handle_terraform_apply)
    mcp.register_tool_handler("terraform_destroy", handle_terraform_destroy)
    mcp.register_tool_handler("terraform_validate", handle_terraform_validate)
    mcp.register_tool_handler("terraform_show", handle_terraform_show)
    mcp.register_tool_handler("terraform_workspace_list", handle_terraform_workspace_list)
    mcp.register_tool_handler("terraform_workspace_select", handle_terraform_workspace_select)
    
    return mcp

def main():
    # Create the MCP server
    mcp = create_mcp_server()
    
    # Start the server
    print("Starting Terraform IAC Assistant MCP server...")
    mcp.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
