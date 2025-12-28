"""
Standalone File Upload Server
Uses FastAPI to provide PDF upload interface
"""
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from upload_handler import upload_handler

app = FastAPI(title="Academic Network - File Upload Service")

# Allow Studio UI cross-origin access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8700", "http://127.0.0.1:8700", "*"],  # Allow all for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile):
    """
    Upload PDF file

    Returns:
        {"success": bool, "task_id": str, "filename": str, "status": str}
    """
    if not file.filename:
        raise HTTPException(400, "Filename cannot be empty")

    # Read file content
    content = await file.read()

    # Call handler
    result = await upload_handler.handle_upload(file.filename, content)

    if not result["success"]:
        raise HTTPException(400, result.get("error", "Upload failed"))

    return JSONResponse(result)

@app.get("/health")
async def health_check():
    """Health check"""
    return {"status": "ok", "service": "upload-service"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "Academic Network - File Upload Service",
        "version": "1.0.0",
        "endpoints": {
            "upload": "POST /upload/pdf",
            "health": "GET /health"
        }
    }

if __name__ == "__main__":
    import uvicorn
    print("=" * 60)
    print("  Academic Network - File Upload Service")
    print("=" * 60)
    print(f"\n  Listening on: http://localhost:8701")
    print(f"  API endpoint: http://localhost:8701/upload/pdf")
    print(f"  Health check: http://localhost:8701/health\n")
    print("  Press Ctrl+C to stop\n")
    print("=" * 60 + "\n")

    uvicorn.run(app, host="localhost", port=8701, log_level="info")
