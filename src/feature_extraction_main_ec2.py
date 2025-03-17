from fastapi import FastAPI
from pydantic import BaseModel

from Comparision import evaluation


app = FastAPI()


class NewsData (BaseModel) :
    title : str
    contents : str


class FeatureResult (BaseModel) :
    probability : float


@app.post("/", response_model = FeatureResult)
async def feature_extraction (data : NewsData) :

    probability = evaluation (data.title, data.contents)
    
    result = {
        "probability" : probability
    }

    return result
