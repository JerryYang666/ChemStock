from fastapi import FastAPI
from pydantic import BaseModel
from ChemSearch import ChemSearch

app = FastAPI()


class RESTapi(BaseModel):
    status: int = 0
    msg: str = ""
    data: dict = {}


class Chemical(BaseModel):
    cas: str = ""
    code: str = ""
    name: str = ""
    weight: float = 0.0
    remaining: int = 0


@app.get("/lookup/cas/{cas}")
async def lookup_cas(cas: str):
    chem = ChemSearch()
    return RESTapi(status=200, msg="OK", data={"ChemName": chem.cas_search(cas)})


@app.get("/lookup/code/{code}")
async def lookup_code(code: str):
    chem = ChemSearch()
    return RESTapi(status=200, msg="OK", data={"ChemName": chem.code_search(code)})


@app.post("/add/chemical")
async def add_chemical(chem: Chemical):
    return RESTapi(status=200, msg="OK", data={"ChemName": chem.name})
