from crud.base import CRUDBase
from models.onlineDictonary import OnlineDictotnary
from schemas.onlineDictonary import OnlineDictonaryCreate, OnlineDictonaryUpdate


class CRUDOnlineDictonary(CRUDBase[OnlineDictonaryUpdate, OnlineDictonaryCreate, OnlineDictonaryUpdate]):
    ...


onlineDictonary = CRUDOnlineDictonary(OnlineDictotnary)
