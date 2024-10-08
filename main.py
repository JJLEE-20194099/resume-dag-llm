from fastapi.responses import StreamingResponse
from typing import Annotated

from fastapi import Response, FastAPI, File, UploadFile, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from llama_cpp import Llama
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from typing import Annotated
import aiofiles
import torch
from transformers import AutoModel, AutoTokenizer, get_linear_schedule_with_warmup, logging
from file_reader import ResumeReader
from src.database.es import Elastic_search
from src.models.cv.info_dto import BatchCVInfo, CVInfo
from src.models.cv.query import CVQuerySchema
from src.utils.wrapper import wrap_id, wrap_resume
from text_extractor import ResumeExtractor
import asyncio
import pandas as pd
from mongoengine import connect
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from fastapi.staticfiles import StaticFiles
import json
import io
from joblib import load, dump

from src.utils.pdf_helper import extract_images

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

load_dotenv(override=True)
connect(db=os.getenv("CV_MONGO_DATABASE"), host=os.getenv("MONGODB_CONNECTION_STRING"))

app = FastAPI()
app.mount("/data/files/cv/page", StaticFiles(directory="./data/files/cv/page"), name="cv page")
app.mount("/data/files/cv/image", StaticFiles(directory="./data/files/cv/image"), name="cv image")


data = [
    {
        "PERSON_NAME": [
            "Nguyen Minh Quan"
        ],
        "JOB_TITLE": [
            "Researcher",
            "Junior Data Scientist"
        ],
        "ORGANIZATION": [
            "HUTECH",
            "University of Natural Science VNUHCM who",
            "University of Technology HUTECH",
            "Tiki Shop"
        ],
        "EDUCATION": [
            "B.E"
        ],
        "MAJOR": [
            "Information Technology",
            "Natural Language Processing"
        ],
        "GPA": [
            "GPA 3.33",
            "GPA 3.8"
        ],
        "SKILL": [
            "AutoML",
            "Heroku",
            "graph theory",
            "Testing",
            "PySpark",
            "BIG DATA",
            "Scrapy A/B",
            "JavaScript",
            "Java",
            "Artificial Intelligence",
            "CMT",
            "Teamworks",
            "R",
            "Powershell",
            "Swimming",
            "Discrete math",
            "Research Presentations",
            "C",
            "Vim",
            "Deep Learning",
            "Scrapping data",
            "visualization",
            "pipeline",
            "Data science",
            "Data structures",
            "Research new technology",
            "Data Visualization and Analysis",
            "Reporting",
            "Communicating",
            "filtering",
            "Time Series",
            "Database Management",
            "Python",
            "Github",
            "HTML",
            "AI",
            "Git",
            "Machine Learning",
            "Analysis",
            "SQL",
            "MARCHINE",
            "clustering algorithms",
            "data analysis",
            "Data Science",
            "NLP",
            "Linear algebra",
            "chatbot",
            "OCR",
            "CSS",
            "Programing",
            "Big Data",
            "Object oriented",
            "Self learning",
            "Writing",
            "Problem solving",
            "Regression",
            "Mathematics",
            "Applied",
            "Calculus",
            "RFM",
            "Statistics",
            "Team leader"
        ],
        "EMAIL": [
            "minhquan23102000@gmail.com"
        ],
        "PROFILE_URL": [
            "github.com"
        ],
        "PHONE": [
            "0383666401"
        ]
    },
    {
        "ORGANIZATION": [
            "VINAI VINGROUP",
            "TOP 7",
            "Front End App",
            "FPT AI CTA Consolation",
            "TOP 24 Makethon",
            "Ba Dam Market Thoi Lai Can Tho City Poem",
            "Scholoship KMS Technology CityNow",
            "Vietnam National University Ho Chi Minh",
            "RUN FOR ORPHANS",
            "HCM CITY UNIVERSITY OF TECHNOLOGY HUTECH"
        ],
        "MAJOR": [
            "Information Technology",
            "Software Technology",
            "Computer Vision"
        ],
        "GPA": [
            "GPA 3.76/4.00",
            "3.97/4.00"
        ],
        "PERSON_NAME": [
            "NGUYEN TRONG NHAN HUTECH",
            "XUAN THOI LAI",
            "MR PHAM"
        ],
        "SKILL": [
            "Statistical Probability",
            "Math",
            "language processor",
            "Run for childrenorphan",
            "Linear",
            "AI Challenge",
            "Scholoship",
            "Collaborator",
            "API building",
            "Identify and extract personal information",
            "Calculus",
            "frameworkTensorflow",
            "Compilation",
            "Computer Vision",
            "BLOG",
            "image analysis",
            "Yolo",
            "Fresher",
            "Logistic vision",
            "Regression",
            "BOT",
            "Linear Algebra",
            "Communication",
            "image processing"
        ],
        "GENDER": [
            "Male"
        ],
        "JOB_TITLE": [
            "professional engineer"
        ],
        "EMAIL": [
            "nguyennhan8521@gmail.com"
        ],
        "PROFILE_URL": [
            "github.com/NTNhacker/DOAN_JAVA",
            "www.youtube.com/watch",
            "fb.com/nhan.n.trong.33",
            "topcv.vn"
        ],
        "PHONE": [
            "0866039411"
        ]
    }
]




def generate_output(inputs):

    conversation = [
        {
            "role": "system",
            "content": f"You are a helpful assistant. Use below information to answer the question from user. \n Information: {str(data)}"
        },
        {
            "role": "user",
            "content": "hi"
        },
        {
            "role": "assistant",
            "content": "how i can help you?"
        },
        {
            "role": "user",
            "content": inputs
        }
    ]
    print("Start to create chat template")
    completion = llm.create_chat_completion(
        messages=conversation,
        stream = True
    )
    print("End to create chat template")

    for i in completion:
        try:
            curr = i['choices'][0]['delta']['content']
            if curr:
                yield str(curr)
        except:pass
    return ""


@app.post("/llm-test")
def main(inputs: str = ""):
    print(inputs)
    return StreamingResponse(generate_output(inputs))

@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    for file in files:
        async with aiofiles.open(f'./data/files/{file.filename}', 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
    return "Uploading Files Done"

@app.post("/llm-test")
def main(inputs: str = ""):
    print(inputs)
    return StreamingResponse(generate_output(inputs))

def load_model():
    model = ResumeExtractor(ner_model_path='./finetuning/spacy/model-best')
    return model

reader = ResumeReader()
extractor = load_model()

def get_info_by_path_util(file_path):
    resume_content = reader.read_text_from_file(file_path)
    resume_summary = extractor.get_summary_from_text(resume_content)
    return resume_summary


def save_info_by_path(file_path_list, batch_id, gender_classify_model, phobert, tokenizer):

    resume_content_list = [reader.read_text_from_file(file_path) for file_path in file_path_list]
    resume_summary_list = [extractor.get_summary_from_text(resume_content, gender_classify_model, phobert, tokenizer) for resume_content in resume_content_list]
    resume_summary_wrapper_list = [wrap_resume(resume) for resume in resume_summary_list]

    image_path_list = [extract_images(file_path) for file_path in file_path_list]

    resume_instances = [CVInfo(**resume, batch_id = batch_id, file_path=f"/data/files/cv/page/{file_path_list[i].split('/')[-1]}", image_paths = [f"/data/files/cv/image/{item.split('/')[-1]}" for item in image_path_list[i]]) for i, resume in enumerate(resume_summary_wrapper_list)]

    cv_ids = CVInfo.objects.insert(resume_instances, load_bulk=False)
    BatchCVInfo.objects(id = batch_id).update(cv_ids = [cv_id for cv_id in cv_ids])

    es_client = Elastic_search()
    es_client.update_cv_data(data = resume_summary_wrapper_list, ids = [str(_) for _ in cv_ids])


async def write_data_util(file:UploadFile):
    file_path = f'./data/files/cv/page/{file.filename}'
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

        return file_path


async def write_data(files: list[UploadFile]):
    tasks = [write_data_util(file) for file in files]
    file_path_list = await asyncio.gather(*tasks)
    # JSONResponse(info_data_list[0])
    return file_path_list

@app.post('/query-cv-list')
async def query_cv(body: CVQuerySchema):
    body = dict(body)
    keys = body.keys()
    filter_body = {
        "query": {
            "bool": {
                "must": []
            }
        }
    }

    for key in keys:
        if body[key]:
            filter_body["query"]["bool"]["must"].append({
                "match": {
                    key: {
                        "query": ", ".join(body[key]),
                        "operator": "OR"
                    }
                }
            })

    es_client = Elastic_search()
    res = es_client.find_documents(index = "cv_data", body = filter_body)

    return res['hits']['hits']




@app.get('/get-cv-list/{batch_id}')
async def get_cv_list_by_batch_id(batch_id:str):
    res = CVInfo.objects(batch_id = ObjectId(batch_id))
    res = res.as_pymongo()
    return [wrap_id(item) for item in res]


@app.get('/get-batch-list')
async def get_batch_list():
    res = BatchCVInfo.objects()
    res = res.as_pymongo()
    return [wrap_id(item) for item in res]

@app.get('/get-cv/{cv_id}')
async def get_cv_by_id(cv_id:str, background_tasks: BackgroundTasks):
    res = CVInfo.objects.get(id=cv_id).to_mongo().to_dict()
    res = wrap_id(res)

    buffer = io.BytesIO()

    with open(res['file_path'], mode='rb') as file:
        buffer.write(file.read())

    background_tasks.add_task(buffer.close)
    headers = {'Content-Disposition': 'inline; filename=f"out.pdf"'}
    return Response(buffer.getvalue(), headers=headers, media_type='application/pdf')

gender_classify_model = load('./name_cls.joblib')

phobert = AutoModel.from_pretrained("./generative_model/phobert_pretrain")
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base-v2")


@app.post("/extract-file-info/")
async def extract_file_info(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
    background_tasks: BackgroundTasks
):
    file_path_list = await write_data(files)

    batch_cv_doc = BatchCVInfo(cv_ids = [])
    batch_data = batch_cv_doc.save()
    batch_id = batch_data.id
    background_tasks.add_task(save_info_by_path, file_path_list = file_path_list, batch_id = batch_id, gender_classify_model=gender_classify_model, phobert=phobert, tokenizer=tokenizer)

    return str(batch_id)


@app.get("/upload-page")
async def get_html():
    content = """
            <body>
            <form action="/extract-file-info/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
            </form>
            </body>
    """
    return HTMLResponse(content=content)