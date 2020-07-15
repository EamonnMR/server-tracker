from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from storage import Game, get_all, create, delete

app = FastAPI()

@app.get("/")
def index():
    # TODO: Render some nice HTML or whatever
    return None

@app.get("/games")
def get_games(type: Optional[str] = None):
    return [
        game for game in 
        get_all()
        if type == game.type or not type
    ]

@app.put("/game")
def add_game(game: Game):
    create(game)

@app.delete("/game")
def delete_game(name: str):
    delete(name)

