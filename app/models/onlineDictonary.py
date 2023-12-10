from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base


class OnlineDictotnary(Base):
    serialNumber = Column(String(9), primary_key=True, index=True)
    category = Column(String(100), nullable=True)
    englishWord = Column(String(255), nullable=False)
    kannadaEquivalent = Column(String(255), nullable=False)
    englishDesc = Column(String(2000), nullable=True)
    kannadaDesc = Column(String(3000),  nullable=False)
    image1 = Column(String(100), nullable=True)
    image2 = Column(String(100), nullable=True)
    moderated = Column(Integer, nullable = False)