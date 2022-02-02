import socket
from typing import List

from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates

from models import User

import webbrowser

app = FastAPI()

import os


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def start():
    #os.system("uvicorn main:app --reload")
    print("client started:....")
    

    webbrowser.open('http://localhost:8000/docs')

start()

