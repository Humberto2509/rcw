from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import subprocess


app = FastAPI()


origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_event():
    subprocess.Popen(["streamlit", "run", "appRF.py"])

if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
