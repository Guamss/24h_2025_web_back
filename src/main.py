import csv
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import ORIGINS, TAGS_METADATA, DESCRIPTION
from models.score import ScoreDTO, ScoreDAO

DATA_PATH = "data/scores.csv"

app = FastAPI(
    openapi_tags=TAGS_METADATA,
    title="API pour le 24h info :-)",
    description=DESCRIPTION,
    summary="La documentation swagger de notre magnifique API",
    version="0.0.1",
    terms_of_service="http://example.com/terms/"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
    Section Score
"""


@app.get("/scores", tags=["Scores"], response_model=list[ScoreDTO])
def list_scores():
    with open(DATA_PATH, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [ScoreDTO(**row) for row in reader]


@app.post("/scores", tags=["Scores"], response_model=ScoreDTO, status_code=201)
def publish_score(score: ScoreDAO):
    if score.score < 0:
        raise HTTPException(status_code=400, detail="Score invalide (doit être positif)")

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    file_exists = os.path.isfile(DATA_PATH)
    with open(DATA_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["name", "score"])
        writer.writerow([score.name, score.score])

    return ScoreDTO(**score.dict())
