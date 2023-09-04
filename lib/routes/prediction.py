from fastapi import APIRouter
from starlette.requests import Request
from time import time
import os
from lib.schemas.prediction import PredictionResult, PredictionScoreResult
from lib.services.encode_anything_core import EncodeAnythingCore
from fastapi import File
from fastapi import FastAPI, UploadFile, Form
from lib.schemas.payload import TextPayload, TextPayload2,TextPayload3
from lib.services.CONFIGS_EATS import EMBED_TEXT_MODEL_CONFIG
path = os.path.dirname(os.path.realpath(__file__))
dir = path.replace('/lib/routes', '/resources')
router = APIRouter()


@router.post("/text_encoder", response_model=PredictionResult, name="text_encoder")
async def encoder_text(request: Request, block_data: TextPayload, MODEL_NAME:str = "luotuo") -> PredictionResult:
    """
    #            - **model**
    - "bge_large_zh_dim": int(1024),

    - "bge_large_zh_noinstruct_dim": int(1024),

    - "bge_base_zh_dim": int(768),

    - "multilingual_e5_large_dim": int(1024),

    - "bge_small_zh_dim": int(512),

    - "m3e_large_dim": int(1024),

    - "m3e_base_dim": int(768),

    - "multilingual_e5_base_dim": int(768),

    - "luotuo_dim": int(1024),

    - "luotuo_en_dim": int(768),

    - "text2vec_large_chinese_dim": int(1024),

    - "text2vec_base_chinese_dim": int(768),

    """
    model: EncodeAnythingCore = request.app.state.model
    s_time = time()
    prediction: list = model.text2embedding(block_data.text, MODEL_NAME)
    yun = time() - s_time
    return PredictionResult(result=prediction, took=yun)

@router.post("/text_similarity", response_model=PredictionScoreResult, name="text_similarity")
async def encoder_text_similarity(request: Request, block_data: TextPayload2, MODEL_NAME:str = "luotuo") -> PredictionScoreResult:
    model: EncodeAnythingCore = request.app.state.model
    s_time = time()
    score: str = model.text2similarity(block_data.text1, block_data.text2,MODEL_NAME)
    yun = time() - s_time
    return PredictionScoreResult(result=score, took=yun)

@router.post("/text_embed_similarity", response_model=PredictionScoreResult, name="text_embed_similarity")
async def encoder_text_embed_similarity(request: Request, block_data: TextPayload3, MODEL_NAME:str = "luotuo") -> PredictionScoreResult:
    model: EncodeAnythingCore = request.app.state.model
    s_time = time()
    score: str = model.text_embed_2similarity(block_data.text1, block_data.embed2, MODEL_NAME)
    yun = time() - s_time
    return PredictionScoreResult(result=score, took=yun)


#  ============================   UE  old===================================
# @router.post("/audio2blendshapes0", response_model=UEResult, name="audio2blendshapes")
# async def audio2blendshapes_encoder0(request: Request, my_file: bytes = File(...), speakEmotion: str ="neutral", ip:str = "192.168.0.172") -> UEResult:
#     """
#            - **audio2face and send to UE over UDP**
#     """
#     model: Audio2FaceCore = request.app.state.model
#     s_time = time()
#     prediction: str = model.wav2bs2ue(my_file,ip)
#     yun = time() - s_time
#     return UEResult(result=prediction, took=yun)



# @router.post("/pic_encoder", response_model=PredictionResult, name="pic_encoder")
# async def pic_encoder(request: Request, my_file: bytes = File(...)) -> PredictionResult:
#     model: EncodeAnythingCore = request.app.state.model
#     s_time = time()
#     prediction: list = model.pic2vec(my_file)
#     yun = time() - s_time
#     return PredictionResult(result=prediction, took=yun)

#
#
# @router.post("/text_encoder", response_model=PredictionResult, name="text_encoder")
# async def sentence_encoder(request: Request, block_data: TextPayload) -> PredictionResult:
#     model: EncodeAnythingCore = request.app.state.model
#     s_time = time()
#     prediction: list = model.text2vec(block_data.text)
#     yun = time() - s_time
#     return PredictionResult(result=prediction, took=yun)
#
#
# @router.post("/text_similarity", response_model=PredictionScoreResult, name="text_similarity")
# async def text_encoder(request: Request, block_data: TextPayload2) -> PredictionScoreResult:

#     model: EncodeAnythingCore = request.app.state.model
#     s_time = time()
#     score: str = model.text_similarity_score(block_data.text1, block_data.text2)
#     yun = time() - s_time
#     return PredictionScoreResult(result=score, took=yun)
#
#
# @router.post("/text_n_embed_similarity", response_model=PredictionScoreResult, name="text_n_embed_similarity")
# async def text_n_embed_encoder(request: Request, block_data: TextPayload2) -> PredictionScoreResult:
#     model: EncodeAnythingCore = request.app.state.model
#     s_time = time()
#     score: str = model.text_n_embed_similarity(block_data.text1, block_data.text2)
#     yun = time() - s_time
#     return PredictionScoreResult(result=score, took=yun)