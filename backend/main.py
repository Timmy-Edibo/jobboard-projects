from fastapi import FastAPI, Body

from core.config import settings


from pydantic import BaseModel
class Post(BaseModel):
    name: str
    content: str

app = FastAPI(title = settings.PROJECT_TITLE, version = settings.PROJECT_VERSION)

@app.get("/")
def post():
    return "Hello World"


@app.post("/post")
def create_post(post: Post):
    return post


@app.delete("/post")
def delete_post(post: Post):

    delete_post
    return post