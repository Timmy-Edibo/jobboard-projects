from operator import ipow
from fastapi import FastAPI, Body

from core.config import settings

from db.session import engine
from db.base_calss import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title = settings.PROJECT_TITLE, version = settings.PROJECT_VERSION)
    create_tables()
    return app


from pydantic import BaseModel


class Post(BaseModel):
    name: str
    content: str

app = start_application()    



@app.get("/")
def post():
    return "Hello World"


@app.post("/post")
def create_post(post: Post):
    return post


