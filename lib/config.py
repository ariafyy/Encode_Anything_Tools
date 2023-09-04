import os



class EnvVars(object):
    # system configuration
    CUDA_VISIBLE_DEVICE = int(os.environ.get("CUDA_VISIBLE_DEVICE", 3))
    region = os.environ.get("REGION", 'cn').lower()
    api_key = os.environ.get('API_KEY', 'convmind')
    APP_VERSION = "0.0.1"
    APP_NAME = "EncodeAnythingTools"
    API_PREFIX = "/encoder"
    DEFAULT_MODEL_PATH = "resources"
    IS_DEBUG = False
