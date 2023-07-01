from fastapi import FastAPI
from api import router

app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})


app.include_router(router)