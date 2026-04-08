from ai.filter import api_call
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class VoiceRequest(BaseModel):
    voice: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/api/voice-command")
async def handle_voice_command(data: VoiceRequest):
    """
    Routes the voice data to the AI service and returns 
    the result to the frontend as is.
    """
    try:
        # Pass the validated JSON/dictionary to your AI function
        # .model_dump() is the Pydantic v2 way to get the dict
        result = await api_call(data.model_dump())

        # Return the AI response directly to the frontend
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"AI Agent Error: {str(e)}")
