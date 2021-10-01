from fastapi import FastAPI

from typing import Optional
from fastapi.param_functions import Body

from pydantic import BaseModel
from pydantic.networks import HttpUrl

from requests import request


app = FastAPI(
    title="CORS Proxy",
    description="Fast Proxy to bypass CORS Policies",
    version="0.0.1",
    contact={
        "name": "Rajesh Joshi",
        "email": "joshirajesh448@gmail.com",
    },
)

# Responses

class IndexResponseModel(BaseModel):
    detail: str = "Please hit any of the following end point with POST Method"
    Version1: str = "/v1"

class V1ResponseModel(BaseModel):
    status_code: int = 200
    payload: dict = {}


# Routes

@app.get(
    "/",
    description='Welcome to CORS Proxy',
    response_model=IndexResponseModel
)
def index():
    return {
        'detail': "Please hit any of the following end point with POST Method",
        'Version1': "/v1"
    }

@app.post("/v1", response_model=V1ResponseModel)
def version1(
    url: HttpUrl = Body(...),
    method: str = Body(
        "GET",
        title='HTTP Method',
        description='Any **Valid HTTP Method** eg. GET, POST, PUT, PATCH, DELETE, etc.'
        ),
    params: Optional[dict] = Body(
        None,
        title='Query Params',
        description='Valid key-value pairs'
        ),
    data: Optional[dict] = Body(
        None,
        title='Request Body/Payload',
        description='Valid JSON'
        ),
    headers: Optional[dict] = Body(
        None,
        title='Request Headers',
        description='Valid key-value pairs'
        ),
    cookies: Optional[dict] = Body(
        None,
        title='Request Cookies',
        description='Valid key-value pairs'
        )
    ):

    try:
        response = request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers,
            cookies=cookies,
        )

        status_code = response.status_code if response.status_code else 200

        return {
            'status_code': status_code,
            'payload': response.json()
        }
    except:
        return {
            'status_code': 500,
            'payload': {
                'detail': 'Internal Server Error'
            }
        }
