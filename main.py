from fastapi import FastAPI

app = FastAPI()


@app.get("/lookup/cas/{cas}")
async def lookup_cas(cas: str):
    return {"message": f"Hello {cas}"}


@app.get("/lookup/code/{code}")
async def lookup_code(code: str):
    return {"message": f"Hello {code}"}
