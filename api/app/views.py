from .models import PredictionRequest
from .utilis import get_model, transform_to_dataframe

model = get_model()
def get_prediction(request:PredictionRequest)->float:
    data_to_predcit = transform_to_dataframe(request)
    prediction = model.predict(data_to_predcit)[0]
    return max(0, prediction)