from fastapi import APIRouter

router = APIRouter()

@router.post("/transcripts")
async def process_transcript():
    return {"message": "Transcript processing endpoint"} 