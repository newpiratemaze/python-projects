from fastapi import FastAPI, Path, Depends
from sqlalchemy.orm import Session
from models import Base, Post
from database import engine, session_local
from schemas import  PostCreate, PostResponse
import random

app = FastAPI()

Base.metadata.create_all(bind= engine)


def get_db():
    db = session_local()
    with db as db:
        yield db

ids = []


@app.post('/posts/', response_model = PostResponse)
async def create_post(post: PostCreate, db:Session = Depends(get_db)) -> PostResponse:
    id = len(ids)
    db_post = PostResponse(id = id, num = 'one')
    ids.append(id)

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post












# @app.get("/")
# async def home():
#     return {"data":"message"}
#
# @app.get("/contacts")
# async def contacts() ->int:
#     return 34
#
#
#
#
#
#
#
# @app.get("/items")
# async def items() -> list[Post]:
#     return [Post(**post) for post in posts]
#
#
# @app.post("/items/add")
# async def add_item(post: PostCreate) -> Post:
#     new_post_id = len(posts)+1
#     new_post = {'id': new_post_id, 'num': post.num}
#     posts.append(new_post)
#     return Post(**new_post)
#
# @app.get("/items/{id}")
# async def items(id:int) -> Post:
#     for post in posts:
#         if post['id'] == id:
#             return Post(**post)
#     else:
#         return "Fuck u!"

