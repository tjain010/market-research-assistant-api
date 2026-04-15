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
    starter_sources: List[SourceItem]          
    report_id: Optional[str] = None            
from typing import List, Optional


class ResearchRequest(BaseModel):
    topic: str


class SourceItem(BaseModel):
    label: str
    url: str


class ResearchPlanResponse(BaseModel):
    report_id: Optional[str] = None         # use for saving memoryfrom pydantic import BaseModel
    topic: str
    research_type: str
    subquestions: List[str]
    report_outline: List[str]
    keywords: List[str]
    next_step: str
    suggested_sources: List[str]            # reponse now includes a list of source objects
    starter_sources: List[SourceItem]