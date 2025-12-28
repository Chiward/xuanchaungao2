from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import shutil
import os
import tempfile
from typing import Optional

from config import get_api_key
from service.parser import parse_file
from service.llm import LLMService
from service.prompts import PROMPT_TEMPLATES

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Services
api_key = get_api_key()
llm_service = None
if api_key:
    llm_service = LLMService(api_key)
else:
    print("WARNING: Deepseek API Key not found! Please set DEEPSEEK_API_KEY in environment or .env.")

class GenerateRequest(BaseModel):
    template_type: str
    topic: str
    time: str
    location: str
    people: str
    content: Optional[str] = ""
    context_text: Optional[str] = ""

@app.get("/health")
def health():
    return {"status": "ok", "llm_ready": llm_service is not None}

@app.get("/templates")
def get_templates():
    return list(PROMPT_TEMPLATES.keys())

@app.post("/parse")
async def parse_document(file: UploadFile = File(...)):
    # Save uploaded file to a temporary file
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    
    try:
        # Parse the file
        text = parse_file(tmp_path)
        return {"filename": file.filename, "content": text}
    except ValueError as ve:
         raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up temp file
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except:
                pass

@app.post("/generate")
async def generate(request: GenerateRequest):
    if not llm_service:
        raise HTTPException(status_code=500, detail="LLM Service not initialized (Missing API Key)")
    
    data = {
        "topic": request.topic,
        "time": request.time,
        "location": request.location,
        "people": request.people,
        "content": request.content
    }
    
    return StreamingResponse(
        llm_service.generate_draft_stream(request.template_type, data, request.context_text),
        media_type="text/event-stream"
    )

if __name__ == "__main__":
    import uvicorn
    # Allow port to be configured via env for Electron
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="127.0.0.1", port=port)
