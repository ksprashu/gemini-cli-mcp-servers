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

### 2. Google OSS Complier (`/google-oss`)

Generates a detailed prompt that instructs Gemini CLI to perform the steps necessary to make a project compliant with Google's open-source standards (adding LICENSE, CONTRIBUTING.md, source headers, etc.).

*   **To Install:**
    ```bash
    fastmcp install gemini-cli google_oss_server/main.py --name google-oss
    ```
*   **Usage:**
    ```
    > /google-oss
    ```

### 3. SuperAgent (`/superagent`)

A powerful orchestrator agent that follows an "Analyze -> Decide -> Formulate -> Delegate" loop to accomplish complex tasks by dispatching specialist agents.

*   **To Install:**
    ```bash
    fastmcp install gemini-cli superagent_server/main.py --name superagent
    ```
*   **Usage:**
    ```
    > /superagent 'your high-level goal here'
    ```

---

## Disclaimer

This is not an officially supported Google product.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.
