from pydantic import BaseModel
from typing import List, Optional
from fastapi import UploadFile

class AnalysisRequest(BaseModel):
    option: str = "other"
    arena_toggled: bool = False
    handicap_goals_winning: float = 0.0
    handicap_goals_losing: float = 0.0
    team1_players: List[str] = ["team 1 player 1", "team 1 player 2", "team 1 player 3", "team 1 player 4"]
    team1_goals: List[float] = [-99, -99, -99, -99]
    team2_players: List[str] = ["team 2 player 1", "team 2 player 2", "team 2 player 3", "team 2 player 4"]
    team2_goals: List[float] = [-99, -99, -99, -99]
    link: Optional[str] = ""

class AnalysisResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
    file_url: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
