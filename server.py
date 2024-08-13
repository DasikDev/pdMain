import uvicorn
import logging
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from main import GptApi

logging.basicConfig(level=logging.INFO)

app = FastAPI()
gpt_api = GptApi()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class createSeoItems(BaseModel):
    productName: str
    words: str


class randomQueryItems(BaseModel):
    query: str


class markAnswerItems(BaseModel):
    mark_text: str
    is_mark: str


class createLogoData(BaseModel):
    prompt: str


@app.post("/api/createSeo")
async def create_seo_api(item: createSeoItems):
    try:
        result = gpt_api.crete_seo(
            name=item.productName, words=item.words
        )
        content = {"status": "ok", "result": result}
        return JSONResponse(content=content, status_code=200)
    except Exception as ex:
        print(ex, "create_seo_api")
        content = {"status": "error", "result": ""}
        return JSONResponse(content=content, status_code=400)


@app.post("/api/randomQuery")
async def random_query_api(item: randomQueryItems):
    try:
        result = gpt_api.random_query(query=item.query)
        content = {"status": "ok", "result": result}
        return JSONResponse(content=content, status_code=200)
    except Exception as ex:
        print(ex, "random_query_api")
        content = {"status": "error", "result": ""}
        return JSONResponse(content=content, status_code=400)


@app.post("/api/markAnswer")
async def mark_answer_api(item: markAnswerItems):
    try:
        result = gpt_api.mark_answer_create(mark_text=item.mark_text, mark_type=item.is_mark)
        content = {"status": "ok", "result": result}
        return JSONResponse(content=content, status_code=200)
    except Exception as ex:
        print(ex, "mark_answer_api")
        content = {"status": "error", "result": ""}
        return JSONResponse(content=content, status_code=400)


@app.post('/api/createLogo')
async def create_logo_api(item: createLogoData):
    try:
        result = gpt_api.create_logo(lolo_prompt=item.prompt)
        content = {"status": "ok", "result": result}
        return JSONResponse(content=content, status_code=200)
    except Exception as ex:
        print(ex, "createLogo")
        content = {"status": "error", "result": ""}
        return JSONResponse(content=content, status_code=400)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
