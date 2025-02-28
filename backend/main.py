from fastapi import FastAPI
from routes import auth, transcripts, insights

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(transcripts.router, prefix="/transcripts")
app.include_router(insights.router, prefix="/insights")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI backend!"} 