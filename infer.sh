#!/bin/bash
export CUDA_VISIBLE_DEVICES=3
cd /home/aria/encode_anything_tools/lib
eval "$(conda shell.bash hook)"
conda activate encode_anything_tools
python main.py
exit 0