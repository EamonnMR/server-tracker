from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from server_tracker.storage import Game, get_all, create, delete

app = FastAPI()

def get_host_ip(request: Request):
    """ Rather than auth, the idea is that you can only affect
    games that you are yourself hosting.
    This attempts to support both local development and prod
    use behind a proxy server."""
    return request.headers.get("X-Real-IP", request.client.host)

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
def add_game(game: Game, request: Request):
    game.address = get_host_ip(request)
    create(game)

@app.delete("/game")
def delete_game(request: Request):
    delete(get_host_ip(request))

