from enum import Enum
from typing import Dict


from sqlalchemy import Column, Enum as EnumSqlAlchemy
from sqlalchemy.orm import relationship

from flask_app.src.database.models.base import BaseModel


class Album(str, Enum):
    seven = 'seven'
    wings = 'wings'


class History(BaseModel):
    __tablename__ = 'history'

    album = Column(EnumSqlAlchemy(Album), nullable=True)
    members = relationship("Member", cascade="all,delete", back_populates="history")

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'album': self.album,
            'members': [member.to_dict() for member in self.members]
            if len(self.historical) > 0
            else None
        }
