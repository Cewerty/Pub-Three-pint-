from fastapi import FastAPI
from app.api.clients import router 

app = FastAPI()

app.include_router(router)

