import pandas as pd
import os
import shutil
import logging
from typing import List, Tuple, Dict, Any
import io
import traceback

from utils.utils import (
    generate_extra_data,
    generate_table_data,
    generate_bar_data,
    get_data,
    save_docx
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        # Ensure static directory exists
        os.makedirs("static", exist_ok=True)
    
    def process_analysis(
        self,
        df: pd.DataFrame,
        filename: str,
        option: str,
        arena_toggled: bool,
        handicap_tuple: Tuple[float, float],
        team1_players: List[str],
        team1_goals: List[float],
        team2_players: List[str],
        team2_goals: List[float],
        link: str
    ) -> Dict[str, Any]:
        """
        Process the sports analysis data and generate results
        """
        try:
            logger.info(f"Starting analysis for file: {filename}")
            logger.info(f"DataFrame shape: {df.shape}")
            logger.info(f"DataFrame columns: {list(df.columns)}")
            logger.info(f"Option: {option}, Arena toggled: {arena_toggled}")
            logger.info(f"Handicap tuple: {handicap_tuple}")
            
            # Generate metadata and chart data
            logger.info("Step 1: Generating extra data...")
            (team1, team2, goals1, goals2,
             club, year, tournament, date_str) = generate_extra_data(df, filename)
            logger.info(f"Generated metadata - Team1: {team1}, Team2: {team2}, Goals: {goals1}-{goals2}")
            
            logger.info("Step 2: Generating table data...")
            title = f"{team1} Vs {team2}"
            table_json = generate_table_data(df)
            logger.info("Table data generated successfully")
            
            logger.info("Step 3: Generating bar data...")
            bar_json = generate_bar_data(df)
            logger.info("Bar data generated successfully")
            
            # Prepare field tuples for processing
            logger.info("Step 4: Preparing field tuples...")
            if arena_toggled:
                fields_tuple_1 = team1_players[:3] + team1_goals[:3]
                fields_tuple_2 = team2_players[:3] + team2_goals[:3]
            else:
                fields_tuple_1 = team1_players + team1_goals
                fields_tuple_2 = team2_players + team2_goals
            logger.info(f"Field tuples prepared - Tuple 1: {fields_tuple_1}, Tuple 2: {fields_tuple_2}")
            
            # Process and enrich data
            logger.info("Step 5: Processing and enriching data...")
            processed = get_data(
                df,
                filename,
                fields_tuple_1,
                fields_tuple_2,
                handicap_tuple,
                toggle_button=option,
                arena_toggled=arena_toggled,
            )
            processed["link"] = link
            logger.info("Data processing completed successfully")
            
            # Generate Word document
            logger.info("Step 6: Generating Word document...")
            save_docx(processed)
            logger.info("Word document generated successfully")
            
            # Ensure static directory exists
            os.makedirs("static", exist_ok=True)
            
            # Copy generated file to static directory for serving
            logger.info("Step 7: Copying file to static directory...")
            if os.path.exists("temp.docx"):
                shutil.copy2("temp.docx", "static/temp.docx")
                logger.info("File copied to static directory successfully")
            else:
                logger.warning("temp.docx file not found after generation")
            
            logger.info("Analysis processing completed successfully")
            
            # Convert numpy types to native Python types for JSON serialization
            def convert_numpy_types(obj):
                if isinstance(obj, dict):
                    return {key: convert_numpy_types(value) for key, value in obj.items()}
                elif isinstance(obj, list):
                    return [convert_numpy_types(item) for item in obj]
                elif hasattr(obj, 'item'):  # numpy scalar
                    return obj.item()
                elif hasattr(obj, 'tolist'):  # numpy array
                    return obj.tolist()
                else:
                    return obj
            
            # Convert processed data to serializable format
            processed_serializable = convert_numpy_types(processed)
            
            return {
                "title": title,
                "table_data": table_json,
                "bar_data": bar_json,
                "team1": team1,
                "team2": team2,
                "goals1": int(goals1) if hasattr(goals1, 'item') else goals1,
                "goals2": int(goals2) if hasattr(goals2, 'item') else goals2,
                "club": club,
                "year": int(year) if hasattr(year, 'item') else year,
                "tournament": tournament,
                "date": date_str,
                "processed_data": processed_serializable
            }
            
        except Exception as e:
            logger.error(f"Analysis processing failed with error: {str(e)}")
            logger.error(f"Full traceback: {traceback.format_exc()}")
            raise Exception(f"Analysis processing failed: {str(e)}")
    
    def get_analysis_summary(self, df: pd.DataFrame, filename: str) -> Dict[str, Any]:
        """
        Get a quick summary of the analysis without full processing
        """
        try:
            (team1, team2, goals1, goals2,
             club, year, tournament, date_str) = generate_extra_data(df, filename)
            
            return {
                "teams": [team1, team2],
                "score": f"{goals1}-{goals2}",
                "club": club,
                "year": year,
                "tournament": tournament,
                "date": date_str
            }
        except Exception as e:
            raise Exception(f"Summary generation failed: {str(e)}")
