from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
import os
import io
import logging
import traceback
from typing import List

from api.models import AnalysisRequest, AnalysisResponse
from services.analysis_service import AnalysisService

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

analysis_router = APIRouter()

@analysis_router.post("/upload", response_model=AnalysisResponse)
async def upload_and_analyze(
    file: UploadFile = File(...),
    option: str = Form("other"),
    arena_toggled: bool = Form(False),
    handicap_goals_winning: float = Form(0.0),
    handicap_goals_losing: float = Form(0.0),
    team1_player1: str = Form("team 1 player 1"),
    team1_player2: str = Form("team 1 player 2"),
    team1_player3: str = Form("team 1 player 3"),
    team1_player4: str = Form("team 1 player 4"),
    team1_goal1: str = Form("-99"),
    team1_goal2: str = Form("-99"),
    team1_goal3: str = Form("-99"),
    team1_goal4: str = Form("-99"),
    team2_player1: str = Form("team 2 player 1"),
    team2_player2: str = Form("team 2 player 2"),
    team2_player3: str = Form("team 2 player 3"),
    team2_player4: str = Form("team 2 player 4"),
    team2_goal1: str = Form("-99"),
    team2_goal2: str = Form("-99"),
    team2_goal3: str = Form("-99"),
    team2_goal4: str = Form("-99"),
    link: str = Form("")
):
    try:
        logger.info(f"Received upload request for file: {file.filename}")
        logger.info(f"File size: {file.size if hasattr(file, 'size') else 'unknown'}")
        logger.info(f"Content type: {file.content_type}")
        
        # Validate file type
        if not file.filename.endswith('.csv'):
            logger.error(f"Invalid file type: {file.filename}")
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        # Read CSV file
        logger.info("Reading CSV file...")
        contents = await file.read()
        logger.info(f"File contents size: {len(contents)} bytes")
        
        df = pd.read_csv(io.BytesIO(contents))
        logger.info(f"DataFrame created successfully. Shape: {df.shape}")
        logger.info(f"DataFrame columns: {list(df.columns)}")
        logger.info(f"First few rows:\n{df.head()}")
        
        # Prepare data for analysis
        logger.info("Preparing data for analysis...")
        team1_players = [team1_player1, team1_player2, team1_player3, team1_player4]
        team1_goals = [team1_goal1, team1_goal2, team1_goal3, team1_goal4]
        team2_players = [team2_player1, team2_player2, team2_player3, team2_player4]
        team2_goals = [team2_goal1, team2_goal2, team2_goal3, team2_goal4]
        
        # Preserve original format of goal values (keep as strings to maintain user input format)
        # The utils functions will handle the conversion when needed for calculations
        
        # Adjust for arena toggle
        if arena_toggled:
            team1_players = team1_players[:3]
            team1_goals = team1_goals[:3]
            team2_players = team2_players[:3]
            team2_goals = team2_goals[:3]
        
        logger.info(f"Team 1 players: {team1_players}")
        logger.info(f"Team 1 goals: {team1_goals}")
        logger.info(f"Team 2 players: {team2_players}")
        logger.info(f"Team 2 goals: {team2_goals}")
        
        # Create analysis service and process data
        logger.info("Creating analysis service...")
        analysis_service = AnalysisService()
        
        logger.info("Starting analysis processing...")
        result = analysis_service.process_analysis(
            df=df,
            filename=file.filename,
            option=option,
            arena_toggled=arena_toggled,
            handicap_tuple=(handicap_goals_winning, handicap_goals_losing),
            team1_players=team1_players,
            team1_goals=team1_goals,
            team2_players=team2_players,
            team2_goals=team2_goals,
            link=link
        )
        
        logger.info("Analysis completed successfully")
        return AnalysisResponse(
            success=True,
            message="Analysis completed successfully",
            data=result,
            file_url=f"/static/temp.docx"
        )
        
    except Exception as e:
        logger.error(f"Upload and analyze failed with error: {str(e)}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@analysis_router.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"static/{filename}"
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")
