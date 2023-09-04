from pydantic import BaseModel

class PredictionResult(BaseModel):
    took: float
    result: list

class PredictionScoreResult(BaseModel):
    took: float
    result: float

class UEResult(BaseModel):
    took: float
    result: str

class UEResult1(BaseModel):
    took: float
    result: str
    clientIP:str