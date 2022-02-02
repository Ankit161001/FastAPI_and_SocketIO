from typing import List

from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates

from models import User

app = FastAPI()


db: List[User] = [
    User(
        first_name= "Ankit",
        last_name= "Rana",
        message= "hello"
    ),
    User(
        first_name= "Nabaneeta",
        last_name= "Roy",
        message= "hii"
    )
]

@app.get("/")
async def home():
    return{"data":"test"}

@app.get("/users")
async def fetch_users():
    return db

@app.post("/users")
async def register_user(user: User):
    db.append(user)