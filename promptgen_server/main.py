# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Annotated

from fastmcp import FastMCP, Message, ToolContext
from pydantic import Field

mcp = FastMCP(
    title="PromptGen Server",
    description="An MCP server to refine user prompts, to be used with Gemini CLI.",
    version="0.1.0",
)

@mcp.prompt
async def prompt(
    context: ToolContext,
    prompt: Annotated[
        str,
        Field(
            description="The user's original prompt. This can be a multi-line string."
        ),
    ],
) -> Message:
    """
    Takes a user's prompt (which can be multi-line) and refines it.

    Args:
        prompt: The user's original prompt.

    Returns:
        A refined prompt.
    """
    prompt_engineering_instructions = '''## Prompt Engineering / Prompt Generation

When creating or building any prompt, use the following structure design effective prompts.

1. Task Context - Start by clearly defining WHO the AI should be and WHAT role it's playing. Don't just say "write an email." Say "You're a senior marketing director writing to the CEO about Q4 strategy."
2. Tone Context - Specify the exact tone. "Professional but approachable" beats "be nice" every time. The more specific, the better the output.
3. Background Data/Documents/Images - Feed the agent with relevant context. Annual reports, previous emails, style guides, whatever's relevant. the Agent can process massive amounts of context and actually uses it.
4. Detailed Task Description & Rules - This is where most people fail. Don't just describe what you want; set boundaries and rules. Eg: "Never exceed 500 words," "Always cite sources," "Avoid technical jargon", "Do not use marketing jargon," "Avoid making assumptions about the user's expertise", etc.
5. Examples - Show, don't just tell. Include 1-2 examples of what good looks like. This dramatically improves consistency.
6. Conversation History - If it's part of an ongoing task, include relevant previous exchanges. the Agent doesn't remember between sessions, so context is crucial.
7. Immediate Task Description - After all that context, clearly state what you want RIGHT NOW. This focuses the Agent's attention on the specific deliverable.
8. Thinking Step-by-Step - Add "Think about your answer first before responding" or "Take a deep breath and work through this systematically." This activates the Agent's reasoning capabilities.
9. Output Formatting - Specify EXACTLY how you want the output structured. Use XML tags, markdown, bullet points, whatever you need. Be explicit.
10. Prefilled Response (Advanced) - Start the agent's response for them. This technique guides the output style and can dramatically improve quality.'''

    # This is the "meta-prompt" that will be generated.
    # It instructs an AI to use the rules to refine the user's original input.
    refined_prompt = f"""
You are a world-class expert in prompt engineering for large language models.
Your task is to take a user's simple, raw prompt and rewrite it into a detailed, effective prompt that will yield superior results.

You must use the following instructions to craft the new prompt. The user's original input should be incorporated into the "Immediate Task Description" part of the new prompt you create.

---
**PROMPT REFINEMENT INSTRUCTIONS:**
{prompt_engineering_instructions}
---

**USER'S RAW PROMPT:**
"{prompt}"

**YOUR TASK:**
Rewrite the user's raw prompt into a new, comprehensive prompt based on the instructions provided. The new prompt should be a complete, self-contained set of instructions for another AI. Structure the output clearly, following the 10-point framework. Fill in the sections with your expert suggestions on what would make the prompt better, but leave placeholders like `[Insert Background Data Here]` or `[Provide Example 1 Here]` where the user needs to supply specific information.
"""

    return Message(content=refined_prompt.strip())