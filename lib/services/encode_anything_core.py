#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
__todo: encode text,img,audio etc
"""
# import os
# worker_id = int(os.getpid()%3)
# DEVICE = f"cuda:{worker_id}"
# print("\033[0;30;44m worker_id: \033[0m ", worker_id)
# print("\033[0;30;44m DEVICE : \033[0m ", DEVICE )
# os.environ["CUDA_VISIBLE_DEVICES"] = str(worker_id)
# os.environ["CUDA_VISIBLE_DEVICES"] = "3"

import torch
# DEVICE = "cuda"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
from sentence_transformers import SentenceTransformer
import numpy as np
from lib.services.CONFIGS_EATS import EMBED_TEXT_MODEL_CONFIG
from torch import Tensor
from lib.services.utils_core import utils_cos_sim
from lib.services.encode_text import EncodeText
from lib.services.encode_img import EncodeImg
from lib.services.encode_audio import EncodeAudio


class MultiSearchCore(object):
    def __init__(self):
        # self.model = SentenceTransformer('resources/clip-ViT-B-32-multilingual-v1')
        self.model = SentenceTransformer('resources/stsb-xlm-r-multilingual')
        # image_features = model.encode_img(image)
        # text_features = model.encode_text(text)
        # audio_features = model.encode_audio(audio)

    def encode_text(self, sents):
        return self.model.encode(sents).tolist()

    def text2vec(self, data):
        embedding = self.model.encode(data)
        embedding = embedding + 1e-10
        sentence_embeddings = embedding / np.linalg.norm(embedding, axis=0)
        return sentence_embeddings.tolist()

    def text_similarity_score(self, query1, query2):
        query1_vec = self.text2vec(query1)
        query2_vec = self.text2vec(query2)
        score = utils_cos_sim(query1_vec, query2_vec)
        return score

    def text_n_embed_similarity(self, query1, query2_vec):
        query1_vec = self.text2vec(query1)
        score = utils_cos_sim(query1_vec, query2_vec)
        return score


class EncodeAnythingCore(object):
    def __init__(self):
        pass
        # image_features = model.encode_img(image)
        # text_features = model.encode_text(text)
        # audio_features = model.encode_audio(audio)

    def text2embedding(self, text, MODEL_NAME):
        res = EncodeText().text2vec(text, MODEL_NAME)
        return res

    def text2similarity(self, query1, query2, MODEL_NAME):
        res = EncodeText().texts_similarity(query1, query2, MODEL_NAME)
        return res

    def text_embed_2similarity(self, query1, embed2, MODEL_NAME):
        res = EncodeText().text_embed_similarity(query1, embed2, MODEL_NAME)
        return res

    def img2embedding(self, data, MODEL_NAME):
        res = EncodeImg().img2vec(data, MODEL_NAME)
        return res

    def audio2embedding(self, data, MODEL_NAME):
        res = EncodeAudio().audio2vec(data, MODEL_NAME)
        return res


if __name__ == '__main__':
    """
    text2vec: 0.5504267
    """
    MODEL_NAME = "luotuo"
    print("text:", len(EncodeAnythingCore().text2embedding("你好", MODEL_NAME)))
