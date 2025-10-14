# Google OSS Compliance Server

An MCP server that generates a detailed prompt for Gemini CLI to make a project compliant with Google's open-source standards.

## Installation

Follow the same steps as the `promptgen_server` to install this server using `gemini mcp add`.

```bash
# From within this directory
gemini mcp add google-oss --cwd . -- 'uvicorn main:mcp --port 8001'
```
Note the use of a different port (`8001`) to avoid conflicts if running multiple servers.

## Usage

In the root directory of the project you want to make compliant, run:

```
> /google-oss
```

This will generate a detailed set of instructions that Gemini CLI will then follow to perform the compliance actions.
