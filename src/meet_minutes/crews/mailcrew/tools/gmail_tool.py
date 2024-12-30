from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from .gmail_utilities import authenticate_gmail, create_draft, create_message
from agentops import record_tool

class GmailToolInput(BaseModel):
    """Input schema for MyCustomTool."""

    body: str = Field(..., description="Description of the argument.")

@record_tool("This is the Gmail tool")
class GmailTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = GmailToolInput

    def _run(self, body: str) -> str:
        try:
            service = authenticate_gmail()
            message = create_message("free.fall.leo@gmail.com", "leoknaw@gmail.com", "Test email", body)
            draft = create_draft(service, "me", message)

            return f"Draft created successfully. Draft id: {draft['id']}"
        except Exception as error:
            return (f'An error occurred: {error}')

