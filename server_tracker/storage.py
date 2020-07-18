import json

import redis
from pydantic import BaseModel
from contextlib import contextmanager

@contextmanager
def redis_conn():
    yield redis.Redis(host='localhost', port=6379, db=0)

class Game(BaseModel):
    port: int
    address: str
    name: str
    type: str

def create(game: Game):
    with redis_conn() as r:
        r.set(game.name, json.dumps(game.dict()))
        return True

def get_all():
    with redis_conn() as r:
        # TODO: Use a pipeline
        return [Game(**json.loads(val)) for val in r.mget(r.keys())]

def delete(name: str):
    with redis_conn() as r:
        return r.delete(name)

