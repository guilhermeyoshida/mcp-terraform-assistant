# MCP Terraform Assistant

An MCP server for managing infrastructure as code using Terraform.

## Features

This MCP server provides an AI agent with tools to interact with Terraform for infrastructure as code management. The agent can:

- Initialize Terraform working directories
- Generate and show execution plans
- Apply changes to infrastructure
- Destroy infrastructure resources
- Validate Terraform configurations
- Show current state or saved plans
- Manage Terraform workspaces

## Prerequisites

- Python 3.10 or higher
- Terraform installed on your system
- [uv](https://github.com/astral-sh/uv) for dependency management

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/guilhermeyoshida/mcp-iac.git
   cd mcp-iac
   ```

2. Install dependencies using uv:
   ```bash
   uv venv
   uv pip install -e .
   ```

## Usage

1. Start the MCP server:
   ```bash
   python main.py
   ```

2. The server will start on `http://0.0.0.0:8000`.

3. Connect to the server using an MCP client:
   ```bash
   mcp connect http://localhost:8000
   ```

4. The AI agent can now use the Terraform tools to help you manage your infrastructure.

## Available Tools

- `terraform_init`: Initialize a Terraform working directory
- `terraform_plan`: Generate and show an execution plan for Terraform
- `terraform_apply`: Apply the changes required to reach the desired state
- `terraform_destroy`: Destroy the infrastructure managed by Terraform
- `terraform_validate`: Validate the syntax and internal consistency of Terraform files
- `terraform_show`: Show the current state or a saved plan
- `terraform_workspace_list`: List Terraform workspaces
- `terraform_workspace_select`: Select a Terraform workspace

## Example Usage

Here's an example of how to use the MCP server with an AI agent:

1. Start the MCP server:
   ```bash
   python main.py
   ```

2. Connect to the server using an MCP client:
   ```bash
   mcp connect http://localhost:8000
   ```

3. The AI agent can now help you with Terraform operations. For example:
   - Initialize a Terraform working directory
   - Generate and review execution plans
   - Apply changes to infrastructure
   - Destroy infrastructure resources
   - Validate Terraform configurations

## Examples

Check out the `examples` directory for sample Terraform configurations that demonstrate how to use the MCP server:

- `examples/aws-s3`: A simple AWS S3 bucket example
