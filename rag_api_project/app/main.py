from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from models.schema import AskRequest, AskResponse
from core.security import verify_api_key
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)


@asynccontextmanager
async def lifestan(app: FastAPI):
    #rag_service.muat_model() 
    yield

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status":"ok"}

@limiter.limit("10/minute")
@app.post("/v1/ask", dependencies=[Depends(verify_api_key)], response_model=AskResponse)
async def tanya(body:AskRequest):
    jawaban = "jawaban adalah"
    #jawaban = rag_service.tanya(body.pertanyaan)
    return {"jawaban": jawaban}

