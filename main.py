from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/")
def hello():
    return JSONResponse(status_code=401, content="Hello")

    
