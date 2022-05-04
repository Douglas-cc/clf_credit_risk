from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates

from infra.sqlalchemy.models import models
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.config.database import engine
from routers import ml


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ml.router)