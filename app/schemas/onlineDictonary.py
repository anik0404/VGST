from typing import Optional

from pydantic import BaseModel
from typing import Sequence


class OnlineDictonaryBase(BaseModel):
    serialNumber: str
    englishWord : str
    kannadaEquivalent : str


# Properties to receive via API on creation
class OnlineDictonaryCreate(OnlineDictonaryBase):
    serialNumber: str
    englishWord : str
    kannadaEquivalent : str
    kannadaDesc : str
    moderated : int

# Properties to receive via API on update
class OnlineDictonaryUpdate(OnlineDictonaryBase):
    ...


class OnlineDictonaryInDBBase(OnlineDictonaryBase):
    serialNumber : Optional[str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class OnlineDictonary(OnlineDictonaryInDBBase):
    pass

class OnlineDictonaryResults(BaseModel):
    results: Sequence[OnlineDictonary]