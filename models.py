from pydantic import BaseModel
from typing import Literal


class Observation(BaseModel):
    subject: str
    body: str
    sender: str

class Action(BaseModel):
    category: Literal["Technical", "Billing", "General"]
    priority: Literal["Low", "Medium", "High"]

class Reward(BaseModel):
    score: float  
    feedback: str