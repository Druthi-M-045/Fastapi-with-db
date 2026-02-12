from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from utils.ai_response import get_completion
from schemas.ai_response_schemas import AIRequest, AIResponse
from schemas.History_schemas import HistoryResponse
from models import History, User
from db import get_db
from dependencies import get_current_user
from repositories.history_repo import HistoryRepo

router = APIRouter()


@router.post("/ask", response_model=AIResponse)
def ask_ai(
    request: AIRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get response from AI model and save to history."""
    try:
        response_text = get_completion(request.message, request.system_prompt)
        
        # Save to history using Repo logic
        history_repo = HistoryRepo(db)
        history_entry = History(
            user_id=current_user.id,
            input_text=request.message,
            output_text=response_text
        )
        history_repo.add_history(history_entry)
        
        return AIResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[HistoryResponse])
def get_history(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get chat history for the current user using Repo logic."""
    history_repo = HistoryRepo(db)
    return history_repo.get_user_history(current_user.id, skip=skip, limit=limit) 