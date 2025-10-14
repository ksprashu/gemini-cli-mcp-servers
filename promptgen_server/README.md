# PromptGen Server

An MCP server for refining user prompts, designed to be used with Gemini CLI.

## Disclaimer

This is not an officially supported Google product. This project is provided for reference and educational purposes only.

## Installation

### 1. Clone the Repository
If you're viewing this file, you've likely already done this. If not, you would clone the repository that contains this server.
```bash
# Replace with the actual repository URL
git clone https://github.com/your-username/your-repo.git
cd your-repo/promptgen_server
```

### 2. Set up the Environment
Navigate to this directory (`/Users/ksprashanth/code/github/gemini-cli-mcp-servers/promptgen_server`) and install the dependencies. It is highly recommended to use a virtual environment.

```bash
# Create and activate a virtual environment
uv venv
source .venv/bin/activate

# Install the server and its dependencies in editable mode
uv pip install -e .
```

### 3. Install to Gemini CLI
To make the `/promptgen` slash command available in your Gemini CLI workspace, you need to register this server. Run the following command from this directory:

```bash
gemini mcp add promptgen --cwd . -- 'uvicorn main:mcp --port 8000'
```
This command tells Gemini CLI:
- `add promptgen`: To add a new server named `promptgen`.
- `--cwd .`: To use the current directory as the working directory.
- `-- 'uvicorn main:mcp --port 8000'`: The command to execute to start the server. Gemini CLI will manage running this process for you.

*For more details on integrations, see the [FastMCP documentation](https://gofastmcp.com/integrations/gemini-cli).*


## Usage
Once installed, Gemini CLI will manage running your server. You can now use the command directly in the CLI:

```
> /promptgen 'write an email to my team about the new project'
```

## Development
If you want to run the server manually for development (for example, to see live logs or use a different port), you can still use the `uvicorn` command directly:
```bash
uvicorn main:mcp --reload --port 8080
```
Note: If you run the server manually, make sure the port matches what you configured in Gemini CLI if you want the CLI to connect to your manual instance.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.
