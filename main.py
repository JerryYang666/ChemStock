from fastapi import FastAPI
from pydantic import BaseModel
from ChemSearch import ChemSearch

app = FastAPI()


class RESTapi(BaseModel):
    status: int = 0
    msg: str = ""
    data: dict = {}


@app.get("/lookup/cas/{cas}")
async def lookup_cas(cas: str):
    chem = ChemSearch()
    return RESTapi(status=200, msg="OK", data={"ChemName": chem.cas_search(cas)})


@app.get("/lookup/code/{code}")
async def lookup_code(code: str):
    chem = ChemSearch()
    return RESTapi(status=200, msg="OK", data={"ChemName": chem.code_search(code)})
