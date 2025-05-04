from pydantic import BaseModel

class PromptRequest(BaseModel):
    topic: str
