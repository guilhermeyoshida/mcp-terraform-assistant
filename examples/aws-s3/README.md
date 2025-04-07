# AWS S3 Bucket Example

This example demonstrates how to use the MCP Terraform IAC Assistant to create and manage an AWS S3 bucket.

## Prerequisites

- AWS credentials configured on your system
- Terraform installed
- MCP Terraform IAC Assistant running

## Using the MCP Server

1. Start the MCP server:
   ```bash
   python main.py
   ```

2. Connect to the server using an MCP client:
   ```bash
   mcp connect http://localhost:8000
   ```

3. Initialize the Terraform working directory:
   ```bash
   mcp terraform_init --working_dir examples/aws-s3
   ```

4. Generate a plan to see what changes will be made:
   ```bash
   mcp terraform_plan --working_dir examples/aws-s3
   ```

5. Apply the changes to create the S3 bucket:
   ```bash
   mcp terraform_apply --working_dir examples/aws-s3 --auto_approve true
   ```

6. Show the current state to see the created resources:
   ```bash
   mcp terraform_show --working_dir examples/aws-s3
   ```

## Customizing the Example

You can customize the example by modifying the variables in `variables.tf` or by passing variables directly to the Terraform commands:

```bash
mcp terraform_plan --working_dir examples/aws-s3 --var '{"bucket_name": "my-custom-bucket", "aws_region": "us-east-1"}'
```

## Cleaning Up

To destroy the created resources:

```bash
mcp terraform_destroy --working_dir examples/aws-s3 --auto_approve true
```

You can also pass variables to the destroy command if needed:

```bash
mcp terraform_destroy --working_dir examples/aws-s3 --var '{"bucket_name": "my-custom-bucket", "aws_region": "us-east-1"}' --auto_approve true
``` 