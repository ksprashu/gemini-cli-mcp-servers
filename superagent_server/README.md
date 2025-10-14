# SuperAgent Server

An MCP server that acts as a master strategist AI developer to accomplish a user's task.

## Installation

Follow the same steps as the other servers to install this using `gemini mcp add`.

```bash
# From within this directory
gemini mcp add superagent --cwd . -- 'uvicorn main:mcp --port 8002'
```
Note the use of a different port (`8002`) to avoid conflicts.

## Usage

In the root directory of the project where you want to run the agent, use the slash command with your high-level goal:

```
> /superagent 'Your high-level goal here'
```
