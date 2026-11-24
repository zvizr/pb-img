import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response

DATA = "ok"


@asynccontextmanager
async def lifespan(_app):
    global DATA
    try:
        with open("/data/probe", "w") as f:
            f.write(str(os.getuid()))
    except OSError:
        DATA = "fail"
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/healthz")
def healthz():
    return {"ok": True}


@app.get("/")
def root():
    return Response(f"PB-IMG {os.getuid()}\ndata={DATA}\n", media_type="text/plain")
