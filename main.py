import os

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy.sql import exists

from schema import Question_num
from models import Question as ModelQuestion

load_dotenv(".env")
app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

def is_question_id_exists(question: dict, model:
ModelQuestion = ModelQuestion) -> bool:
    return db.session.query(
        exists().where(model.question_id == question["id"])
    ).scalar()


def get_last_question(model: ModelQuestion = ModelQuestion) -> ModelQuestion:
    return db.session.query(model).order_by(model.id.desc()).first()