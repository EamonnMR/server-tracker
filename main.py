from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Game(BaseModel):
    port: int
    address: str
    name: str
    type: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/games")
def get_games(type: Optional[string] = None):
    return { "query": "select * from games"}

@app.put("/game"):
def add_game(game: Game):
    return { "query": "insert ({', '.join([v for k, v in game])}) into games"}

