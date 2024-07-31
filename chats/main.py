from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Example</title>
    </head>
    <body>
        <h1>WebSocket Example</h1>
        <input id="messageInput" type="text" autocomplete="off"/>
        <button onclick="sendMessage()">Send</button>
        <ul id="messages">
        </ul>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");

            ws.onmessage = function(event) {
                const messages = document.getElementById('messages');
                const message = document.createElement('li');
                message.textContent = event.data;
                messages.appendChild(message);
            };

            function sendMessage() {
                const input = document.getElementById("messageInput");
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
