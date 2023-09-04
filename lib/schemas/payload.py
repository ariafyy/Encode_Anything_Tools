from typing import List, Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, Form


class TextPayload(BaseModel):
    text: Union[str]

class TextPayload2(BaseModel):
    text1: Union[str]
    text2: Union[str]

class TextPayload3(BaseModel):
    text1: Union[str]
    embed2:List[float]

def payload_to_list(hpp: TextPayload) -> List:
    return [hpp.text]
