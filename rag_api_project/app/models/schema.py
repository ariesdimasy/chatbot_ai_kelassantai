from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    pertanyaan:str = Field(
        ...,
        min_length=3,
        max_length=500
    )
    top_k: int = Field(
        default=2,
        ge=1, # minimal 1
        le = 5, # maksimal 5
    )

class AskResponse(BaseModel):
    jawaban: str