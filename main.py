import subprocess
from typing import List, Dict, Any

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("terraform-assistant")

# Define the tools for Terraform operations
@mcp.tool()
async def terraform_init(working_dir: str, backend_config: Dict[str, Any] = None) -> str:
    """Initialize a Terraform working directory.
    
    Args:
        working_dir: Path to the Terraform working directory
        backend_config: Backend configuration for Terraform
    """
    if backend_config is None:
        backend_config = {}
    
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
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
async def terraform_plan(working_dir: str, var_file: str = None, var: Dict[str, Any] = None) -> str:
    """Generate and show an execution plan for Terraform.
    
    Args:
        working_dir: Path to the Terraform working directory
        var_file: Path to a variables file
        var: Variables to set for the Terraform plan
    """
    if var is None:
        var = {}
    
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
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
async def terraform_apply(working_dir: str, auto_approve: bool = False, var_file: str = None, var: Dict[str, Any] = None) -> str:
    """Apply the changes required to reach the desired state of the configuration.
    
    Args:
        working_dir: Path to the Terraform working directory
        auto_approve: Skip interactive approval of plan before applying
        var_file: Path to a variables file
        var: Variables to set for the Terraform apply
    """
    if var is None:
        var = {}
    
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
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
async def terraform_destroy(working_dir: str, auto_approve: bool = False, var_file: str = None, var: Dict[str, Any] = None) -> str:
    """Destroy the infrastructure managed by Terraform.
    
    Args:
        working_dir: Path to the Terraform working directory
        auto_approve: Skip interactive approval of plan before destroying
        var_file: Path to a variables file
        var: Variables to set for the Terraform destroy
    """
    if var is None:
        var = {}
    
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
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
async def terraform_validate(working_dir: str) -> str:
    """Validate the syntax and internal consistency of Terraform files.
    
    Args:
        working_dir: Path to the Terraform working directory
    """
    try:
        result = subprocess.run(
            ["terraform", "validate"],
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
async def terraform_show(working_dir: str, plan_file: str = None) -> str:
    """Show the current state or a saved plan.
    
    Args:
        working_dir: Path to the Terraform working directory
        plan_file: Path to a saved plan file
    """
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
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
async def terraform_workspace_list(working_dir: str) -> str:
    """List Terraform workspaces.
    
    Args:
        working_dir: Path to the Terraform working directory
    """
    try:
        result = subprocess.run(
            ["terraform", "workspace", "list"],
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
async def terraform_workspace_select(working_dir: str, name: str) -> str:
    """Select a Terraform workspace.
    
    Args:
        working_dir: Path to the Terraform working directory
        name: Name of the workspace to select
    """
    try:
        result = subprocess.run(
            ["terraform", "workspace", "select", name],
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting Terraform Assistant MCP server...")
    mcp.run(transport='stdio')
