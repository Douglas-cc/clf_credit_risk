import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.wsgi import WSGIMiddleware

from infra.sqlalchemy.models import models
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.config.database import engine
from routers import ml


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ml.router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)