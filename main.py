import asyncio
from datetime import datetime

from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.get('/')
def root():
    return 'Connect to /current_time endpoint to get actual time'


@app.websocket('/current_time')
async def current_time(websocket: WebSocket):
    await websocket.accept()

    while True:
        await asyncio.sleep(1)
        await websocket.send_text(str(datetime.now()))
