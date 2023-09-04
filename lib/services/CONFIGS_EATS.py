#!/usr/bin/env python
# -*- coding:utf-8 -*-


import socket
HOST_NAME = socket.gethostname()
if HOST_NAME == "Aria":
    RESOURCES_DIR = "/xxx/resources"
else:
    print("HOST_NAME:", HOST_NAME)

EMBED_TEXT_MODEL_bge_large_zh = RESOURCES_DIR +"/embed/bge-large-zh"
EMBED_TEXT_MODEL_bge_large_zh_noinstruct = RESOURCES_DIR +"/embed/bge-large-zh-noinstruct"
EMBED_TEXT_MODEL_bge_base_zh = RESOURCES_DIR +"/embed/bge-base-zh"
EMBED_TEXT_MODEL_multilingual_e5_large = RESOURCES_DIR +"/embed/multilingual-e5-large"
EMBED_TEXT_MODEL_bge_small_zh = RESOURCES_DIR +"/embed/bge-small-zh"
EMBED_TEXT_MODEL_m3e_large = RESOURCES_DIR +"/embed/m3e-large"
EMBED_TEXT_MODEL_m3e_base = RESOURCES_DIR +"/embed/m3e-base"
EMBED_TEXT_MODEL_multilingual_e5_base = RESOURCES_DIR +"/embed/multilingual-e5-base"
EMBED_TEXT_MODEL_luotuo = RESOURCES_DIR + "/embed/luotuo-bert-medium"
EMBED_TEXT_MODEL_luotuo_en = RESOURCES_DIR + "/embed/luotuo-bert-en"
EMBED_TEXT_MODEL_text2vec_large = RESOURCES_DIR +"/embed/text2vec-large-chinese"
EMBED_TEXT_MODEL_text2vec_base = RESOURCES_DIR +"/embed/text2vec-large-base"

EMBED_TEXT_MODEL_CONFIG = {
    "bge_large_zh": EMBED_TEXT_MODEL_bge_large_zh,
    "bge_large_zh_dim": int(1024),
    "bge_large_zh_noinstruct": EMBED_TEXT_MODEL_bge_large_zh_noinstruct,
    "bge_large_zh_noinstruct_dim": int(1024),
    "bge_base_zh": EMBED_TEXT_MODEL_bge_base_zh,
    "bge_base_zh_dim": int(768),
    "multilingual_e5_large": EMBED_TEXT_MODEL_multilingual_e5_large,
    "multilingual_e5_large_dim": int(1024),
    "bge_small_zh": EMBED_TEXT_MODEL_bge_small_zh,
    "bge_small_zh_dim": int(512),
    "m3e_large": EMBED_TEXT_MODEL_m3e_large,
    "m3e_large_dim": int(1024),
    "m3e_base": EMBED_TEXT_MODEL_m3e_base,
    "m3e_base_dim": int(768),
    "multilingual_e5_base": EMBED_TEXT_MODEL_multilingual_e5_base,
    "multilingual_e5_base_dim": int(768),
    "luotuo": EMBED_TEXT_MODEL_luotuo,
    "luotuo_dim": int(1024),
    "luotuo_en": EMBED_TEXT_MODEL_luotuo_en,
    "luotuo_en_dim": int(768),
    "text2vec_large_chinese": EMBED_TEXT_MODEL_text2vec_large,
    "text2vec_large_chinese_dim": int(1024),
    "text2vec_base_chinese": EMBED_TEXT_MODEL_text2vec_base,
    "text2vec_base_chinese_dim": int(768),
  }
FASTAPI_PORT_EMBED = 8300
