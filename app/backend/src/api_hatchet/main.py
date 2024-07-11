import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn
from dotenv import load_dotenv
import json
import time

from hatchet_sdk import Hatchet

from .models import MessageRequest


load_dotenv()

app = FastAPI()

hatchet = Hatchet()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]

from .service import create

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/message")
def message(data: MessageRequest):
    print("calling workflow")
    workflow_run_id = create(state="initial")
    return {"messageId": workflow_run_id}


def start():
    uvicorn.run("src.api_hatchet.main:app", host="0.0.0.0", port=8000, reload=True)
