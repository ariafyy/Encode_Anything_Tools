#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
__ToDo："EncodeText"
__uodate_info: ""
"""

import torch
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
from sentence_transformers import SentenceTransformer
import numpy as np
from lib.services.utils_core import utils_cos_sim
from lib.services.CONFIGS_EATS import EMBED_TEXT_MODEL_CONFIG


class EncodeText(object):
    def __init__(self):
        pass

    def model_name2path(self, MODEL_NAME):
        MODEL_PATH = EMBED_TEXT_MODEL_CONFIG[MODEL_NAME]
        return MODEL_PATH

    def load_model(self, MODEL_NAME):
        MODEL_PATH = self.model_name2path(MODEL_NAME)
        self.model = SentenceTransformer(MODEL_PATH, device=DEVICE)
        return self.model

    def text2vec(self, data, MODEL_NAME):
        self.model = self.load_model(MODEL_NAME)
        embedding = self.model.encode(data)
        embedding = embedding + 1e-10
        sentence_embeddings = embedding / np.linalg.norm(embedding, axis=0)
        return sentence_embeddings.tolist()

    def get_embed_dim(self, data, MODEL_NAME):
        dimensions = len(self.text2vec(data, MODEL_NAME))
        return dimensions

    def texts_similarity(self, query1, query2, MODEL_NAME):
        query1_vec = self.text2vec(query1, MODEL_NAME)
        query2_vec = self.text2vec(query2, MODEL_NAME)
        score = utils_cos_sim(query1_vec, query2_vec)
        return score

    def text_embed_similarity(self, query1, embed2, MODEL_PATH):
        query1_vec = self.text2vec(query1, MODEL_PATH)
        score = utils_cos_sim(query1_vec, embed2)
        return score


if __name__ == '__main__':
    """
    """
    MODEL_NAME = "luotuo_en"
    print("\033[0;30;43m similarity: \033[0m ",EncodeText().texts_similarity("你好", "您好", MODEL_NAME))
    print("\033[0;30;43m dimisions: \033[0m ", EncodeText().get_embed_dim("data", MODEL_NAME), '\n')
