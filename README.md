# Encode_Anything_Tools

**Convert text/ img/ audio  into embeddings**

EATS(encode_anything_tools): an AI tool from Aria that can encode any object, in any image/audio/text, with a single click...

This idea is inspired by SAM (Segment Anything Model) from Meta.

## encode everything 2 embeddings:

- encode text,img,audio etc



# Ignore the following:
**As some model is in accordance with the technical specifications of huggingface, but not in sentence transformer, you will see the following warning, it is OK to run, just ignore it.**
'''
No sentence-transformers model found with name XXXXXXX. Creating a new one with MEAN pooling.

Some weights of BertModel were not initialized from the model checkpoint at XXXXXXX and are newly initialized: ['bert.pooler.dense.weight', 'bert.pooler.dense.bias']

You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
'''


## embedding compare
- [sbert_author_blog](https://medium.com/@nils_reimers/openai-gpt-3-text-embeddings-really-a-new-state-of-the-art-in-dense-text-embeddings-6571fe3ec9d9)

## [Leaderboard](https://github.com/FlagOpen/FlagEmbedding/blob/master/C_MTEB/README.md#leaderboard)

| Model | Embedding dimension | Avg | Retrieval | STS | PairClassification | Classification | Reranking | Clustering |
|:-------------------------------|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| [**bge-large-zh**](https://huggingface.co/BAAI/bge-large-zh) | 1024 | **64.20** | **71.53** | **54.98** | **78.94** | 68.32 | **65.11** | 48.39 |
| [bge-large-zh-noinstruct](https://huggingface.co/BAAI/bge-large-zh-noinstruct) | 1024 | 63.53 | 70.55 | 53 | 76.77 | **68.58** | 64.91 | **50.01** |
| [BAAI/bge-base-zh](https://huggingface.co/BAAI/bge-base-zh) | 768 | 62.96 | 69.53 | 54.12 | 77.5 | 67.07 | 64.91 | 47.63 |
| [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large) | 1024 | 58.79 | 63.66 | 48.44 | 69.89 | 67.34 | 56.00 | 48.23 |
| [BAAI/bge-small-zh](https://huggingface.co/BAAI/bge-small-zh) | 512 | 58.27 |  63.07 | 49.45 | 70.35 | 63.64 | 61.48 | 45.09 |
| [m3e-base](https://huggingface.co/moka-ai/m3e-base) | 768 | 57.10 | 56.91 | 50.47 | 63.99 | 67.52 | 59.34 | 47.68 |
| [m3e-large](https://huggingface.co/moka-ai/m3e-large) | 1024 |  57.05 | 54.75 | 50.42 | 64.3 | 68.2 | 59.66 | 48.88 |
| [multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) | 768 | 55.48 | 61.63 | 46.49 | 67.07 | 65.35 | 54.35 | 40.68 |
| [multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) | 384 | 55.38 | 59.95 | 45.27 | 66.45 | 65.85 | 53.86 | 45.26 |
| [text-embedding-ada-002(OpenAI)](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings) | 1536 |  53.02 | 52.0 | 43.35 | 69.56 | 64.31 | 54.28 | 45.68 |
| [luotuo](https://huggingface.co/silk-road/luotuo-bert-medium) | 1024 | 49.37 |  44.4 | 42.78 | 66.62 | 61 | 49.25 | 44.39 |
| [text2vec-base](https://huggingface.co/shibing624/text2vec-base-chinese) | 768 |  47.63 | 38.79 | 43.41 | 67.41 | 62.19 | 49.45 | 37.66 |
| [text2vec-large](https://huggingface.co/GanymedeNil/text2vec-large-chinese) | 1024 | 47.36 | 41.94 | 44.97 | 70.86 | 60.66 | 49.16 | 30.02 |



# RUN step by step
#### step by step

- conda create -n encode_anything_tools python=3.9.16

- pip install -r requirements.txt

- CUDA_VISIBLE_DEVICES=3 python main.py

### method1
- bash infer.sh

### method2
- cd /home/aria/encode_anything_tools/lib

- conda activate encode_anything_tools

- nohup python main.py >eats.log 2>&1 &

- lsof -i:8300


=

# Roadmap
