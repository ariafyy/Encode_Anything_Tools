"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

uvicorn main:app --reload
"""




import os,sys
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
def get_paths():
    currentPath = os.getcwd()
    print("\033[0;30;42m current    path: \033[0m ", currentPath)
    parentPath = os.path.abspath(__file__ + "/../../")
    print("\033[0;30;43m parent     path: \033[0m ", parentPath)
    grandparentPath = os.path.abspath(__file__ + "/../../../")
    print("\033[0;30;45m grandparent path: \033[0m ", grandparentPath)
    sys.path.append(currentPath)
    if currentPath.endswith("lib"):
        sys.path.append(currentPath+"/services")
    sys.path.append(parentPath)
    sys.path.append(grandparentPath)
    print("\n\n\033[0;30;43m sys.path: \033[0m ", sys.path)
    return currentPath, parentPath, grandparentPath
get_paths()
from fastapi import FastAPI
from lib.routes.router import api_router
from lib.config import EnvVars
from lib.event_handlers import (start_app_handler, stop_app_handler)



def get_app() -> FastAPI:
    fast_app = FastAPI(title=EnvVars.APP_NAME, version=EnvVars.APP_VERSION, debug=EnvVars.IS_DEBUG,workers=4)
    fast_app.include_router(api_router, prefix=EnvVars.API_PREFIX)
    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))
    return fast_app


app = get_app()



if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "3"
    import uvicorn
    from lib.services.CONFIGS_EATS import FASTAPI_PORT_EMBED
    app = get_app()
    uvicorn.run(app, host="0.0.0.0", port=FASTAPI_PORT_EMBED)
