from models import History
from sqlalchemy.orm import Session
from typing import List

class HistoryRepo:
    def __init__(self, db: Session):
        self.db = db

    def add_history(self, history_entry: History) -> History:
        self.db.add(history_entry)
        self.db.commit()
        self.db.refresh(history_entry)
        return history_entry

    def get_user_history(self, user_id: int, skip: int = 0, limit: int = 100) -> List[History]:
        return self.db.query(History).filter(History.user_id == user_id).offset(skip).limit(limit).all()
