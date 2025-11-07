# Gemini CLI MCP Servers

This repository contains a collection of custom MCP (Multi-Capability Provider) servers designed to extend the functionality of the Gemini CLI.

## Initial Project Setup

Before installing the individual servers, it's recommended to set up the project environment.

1.  **Clone the Repository (if you haven't already):**
    ```bash
    # Replace with the actual repository URL
    git clone https://github.com/your-username/gemini-cli-mcp-servers.git
    cd gemini-cli-mcp-servers
    ```

2.  **Set up the Virtual Environment:**
    This project uses `uv` for environment and package management.
    ```bash
    # Create and activate a virtual environment
    uv venv
    source .venv/bin/activate

    # Install base dependencies
    uv pip install -e .
    ```

---

## Available Servers

Below is a list of the available servers and how to install them into the Gemini CLI. The recommended installation method is using the `fastmcp` command-line tool.

### 1. PromptGen (`/promptgen`)

An MCP server to help refine user prompts based on a set of prompt engineering best practices.

*   **To Install:**
    ```bash
    fastmcp install gemini-cli promptgen_server/main.py --name promptgen
    ```
*   **Usage:**
    ```
    > /promptgen 'your simple prompt idea'
    ```

### 2. SuperAgent (`/superagent`)

A powerful orchestrator agent that follows an "Analyze -> Decide -> Formulate -> Delegate" loop to accomplish complex tasks by dispatching specialist agents.

*   **To Install:**
    ```bash
    fastmcp install gemini-cli superagent_server/main.py --name superagent
    ```
*   **Usage:**
    ```
    > /superagent 'your high-level goal here'
    ```

**Important Setup for SuperAgent:**

The SuperAgent requires a dedicated temporary directory for its operations. Please create the following directory in your home directory:

```bash
mkdir -p ~/tmp/gemini-tasks/
```

Additionally, you must inform the Gemini CLI about this new directory so it can write scratch files outside the current working directory. You can do this in one of two ways:

1.  **Using the Gemini CLI command:**
    ```bash
    /directory add ~/tmp/gemini-tasks/
    ```
2.  **Manually editing `settings.json`:**
    Add the following entry to your `settings.json` file, located in your `.gemini/` folder:
    ```json
      "context": {
        "ignore": [],
        "includeDirectories": [
          "/Users/ksprashanth/tmp/gemini-tasks"
        ]
      },
    ```
    (Note: Replace `/Users/ksprashanth/tmp/gemini-tasks` with the actual absolute path to your `gemini-tasks` directory if it's different.)

---

## Disclaimer

This is not an officially supported Google product.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.
