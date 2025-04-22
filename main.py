from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()  # Create a FastAPI app instance

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None

my_list = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2},
    {"title": "title of post 3", "content": "content of post 3", "id": 4}
    
]

@app.get("/posts")
def get_all_posts():
    return my_list

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_list.append(post_dict)
    return post_dict

@app.get("/posts/latest")
def get_latest_post():
    return my_list[-1]

@app.get("/posts/{id}")
def get_post_by_id(id: int):
    post = find_post(id)
    if post:
        return post
    return {"error": "Post not found"}

@app.delete("/posts/{id}")
def delete_post(id: int):
    indx = find_index_post(id)
    if indx is not None:
        my_list.pop(indx)
        return {"message": f"Post with ID {id} successfully deleted"}
    return {"error": "Post not found"}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    indx = find_index_post(id)
    if indx is not None:
        post_dict = post.dict()
        post_dict['id'] = id
        my_list[indx] = post_dict
        return {"message": f"Post with ID {id} successfully updated"}
    return {"error": "Post not found"}

def find_post(id):
    for p in my_list:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_list):
        if p['id'] == id:
            return i
        
