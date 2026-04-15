from pydantic import BaseModel
from typing import List


class ResearchRequest(BaseModel):
    topic: str


# structure of one source entry
class SourceItem(BaseModel):
    label: str
    url: str

class ResearchPlanResponse(BaseModel):
    topic: str
    research_type: str
    subquestions: List[str]
    report_outline: List[str]
    keywords: List[str]
    next_step: str
    suggested_sources: List[str]               
    starter_sources: List[SourceItem]          # reponse now includes a list of source objects