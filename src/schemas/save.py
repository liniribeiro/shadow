from typing import Dict, Union

from pydantic import BaseModel


class SaveInput(BaseModel):
    data: Dict = None
