import asyncio
from fastapi import FastAPI
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from tradingview_mcp.server import server

app = FastAPI(title="Kairos TV Bridge")
sse = SseServerTransport("/messages")

@app.get("/sse")
async def endpoint():
    async with sse.connect_scope() as scope:
        await server.run(
            sse.read_stream,
            sse.write_stream,
            server.create_initialization_options()
        )

@app.post("/messages")
async def messages():
    await sse.handle_post_request()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

