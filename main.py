import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stocks = ["AAPL", "MSFT", "NVDA", "SHOP.TO", "TD.TO"]

def generate_data():
    data = []
    for s in stocks:
        score = random.randint(40, 95)
        rec = "BUY" if score > 75 else "HOLD" if score > 50 else "AVOID"
        data.append({
            "ticker": s,
            "score": score,
            "recommendation": rec
        })
    return data

@app.get("/")
def root():
    return {"status": "running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_json(generate_data())
        await asyncio.sleep(3)
