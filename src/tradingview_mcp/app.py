from fastapi import FastAPI
from mcp.server.sse import SseServerTransport
from tradingview_mcp.server import server

app = FastAPI(title="Kairos Market Intelligence")
sse = SseServerTransport("/messages")

@app.get("/")
async def root():
    """Root endpoint for status verification"""
    return {
        "status": "online",
        "system": "Kairos Market Intelligence",
        "endpoints": ["/sse", "/messages", "/health"]
    }

@app.get("/health")
async def health():
    """Health check for Render/Koyeb"""
    return {"status": "healthy"}

@app.get("/sse")
async def endpoint():
    """Main MCP SSE entry point"""
    async with sse.connect_scope() as scope:
        await server.run(
            sse.read_stream,
            sse.write_stream,
            server.create_initialization_options()
        )

@app.post("/messages")
async def messages():
    """Handle MCP client messages"""
    await sse.handle_post_request()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

