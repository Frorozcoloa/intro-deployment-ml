from matplotlib.pyplot import title
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    opening_gross:float
    screens:float
    production_budget:float
    title_year:int
    aspect_radio:float
    duration:int
    cast_total_facebook_likes:float
    budget:float
    imdb_score: float

class PredictionResponse(BaseModel):
    wordwide_gross:float