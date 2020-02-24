
from enum import Enum
from typing import Dict


from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database.models.base import BaseModel


class Album(str, Enum):
    seven = 'seven'
    wings = 'wings'


class Member(BaseModel):
    __tablename__ = 'member'

    history_id = Column(UUID(as_uuid=True), ForeignKey('history.id'), nullable=False)
    history = relationship('History', back_populates="members")

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'history_id': self.history_id,
        }
