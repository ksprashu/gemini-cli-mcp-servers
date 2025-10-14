from fastmcp import FastMCP, Message, ToolContext

mcp = FastMCP(
    title="Google OSS Compliance Server",
    description="Generates a detailed prompt to make a project compliant with Google's open-source standards.",
    version="0.1.0",
)

@mcp.prompt
async def google_oss(context: ToolContext) -> Message:
    """
    Generates a detailed prompt for Gemini CLI to make the current project
    Google Open Source compliant.
    """
    instructions_for_gemini = '''
You are about to make the current project compliant with Google's Open Source standards. Follow these steps precisely.

**1. Define Target Project:**
The target project is the current working directory. Acknowledge this directory.

**2. Clone Reference Template:**
Clone the `https://github.com/google/new-project` repository into a temporary directory. Use `/Users/ksprashanth/tmp/gemini-tasks/` as the base for this temporary directory.
Example command: `git clone https://github.com/google/new-project /Users/ksprashanth/tmp/gemini-tasks/google-oss-template`

**3. Add Core Files:**
- Read the content of the `LICENSE` file from the template repo.
- Write this content to a new `LICENSE` file in the root of the target project.
- Read the content of the `CONTRIBUTING.md` file from the template repo.
- Write this content to a new `CONTRIBUTING.md` file in the root of the target project.

**4. Add Source Code License Headers:**
- **Identify Source Files:** Find all source code files in the target project. You should look for common extensions like `.py`, `.js`, `.ts`, `.java`, `.go`, `.c`, `.h`, `.cpp`, `.sh`, `.rb`, `.rs`. Be mindful not to add headers to data files like `.json` or `.md`.
- **Define Language-Specific Headers:** Create the standard Apache 2.0 license header, but adapt the comment syntax for each programming language.
    - Python (`.py`): `#`
    - JavaScript/Java/Go/etc. (`.js`, `.ts`, `.java`, `.go`, `.c`, `.cpp`): `/* ... */`
    - Shell (`.sh`): `#`
- **Prepend Headers:** For each identified source file:
    a. Read the existing content of the file.
    b. Check if the license header is already present. If so, skip the file.
    c. Prepend the correct, language-specific license header to the top of the file content. Use the current year for the copyright notice.
    d. Overwrite the file with the new content (header + original content).

**5. Update README.md:**
- Read the `README.md` file from the target project. If it doesn't exist, create one.
- Add the following sections to the file:
    ```markdown
    ## Disclaimer

    This is not an officially supported Google product.

    ## License

    This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.
    ```
- If the README already contains these sections, ensure they are up-to-date.

**6. Clean Up:**
- Remove the temporary directory containing the cloned template repo.

Execute this plan step-by-step, explaining each major action before you take it.
'''
    return Message(content=instructions_for_gemini.strip())
