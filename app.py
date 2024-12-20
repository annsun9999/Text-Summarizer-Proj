from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textsummarizer.pipeline.prediction import PredictionPipeline

text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successfully") 
    
    except Exception as e:
        return Response(f"Error Occurred!{str(e)}")
    
@app.get("/predict")
async def predict(text):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return result
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)