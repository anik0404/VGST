from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends

from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session

from schemas.onlineDictonary import OnlineDictonaryResults, OnlineDictonary, OnlineDictonaryCreate

import deps
import crud
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent


app = FastAPI(title="Online Dictonary API", openapi_url="/openapi.json")

api_router = APIRouter()



@api_router.get("/", status_code=200)
def root(
    request: Request,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Root GET
    """
    onlineDictonary = crud.onlineDictonary.get_multi(db=db,skip=0, limit=10)
    return {"results": onlineDictonary}


@api_router.get("/dictonary/{englishWord}", status_code=200, response_model=OnlineDictonary)
def fetch_recipe(
    *,
    englishWord: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch dictonary by englush word
    """
    result = crud.onlineDictonary.get(db=db, id=englishWord)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Matching word for englishWord {englishWord} not  found"
        )

    return result


@api_router.get("/search/", status_code=200, response_model=OnlineDictonaryResults)
def search_recipes(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="mango"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for recipes based on label keyword
    """
    dictonaryList = crud.onlineDictonary.get_multi(db=db, limit=max_results)
    if not keyword:
        return {"results": dictonaryList}

    results = filter(lambda onlineDictonary: keyword.lower() in onlineDictonary.englishWord.lower(), dictonaryList)
    return {"results": list(results)[:max_results]}


@api_router.post("/dictonary/", status_code=201, response_model=OnlineDictonary)
def submit_translation(
    *, dictonary_in: OnlineDictonaryCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Submit a new translation entry in the database.
    """
    dictonary_input = crud.onlineDictonary.create(db=db, obj_in=dictonary_in)

    return dictonary_input


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="210.212.207.214", port=8001, log_level="debug")
