from fastapi import FastAPI
from pydantic import BaseModel
from app.prediction import run_prediction

app = FastAPI()

class InputFileParameters(BaseModel):
    month: str
    year: str

class OutputPredParameters(BaseModel):
    pred_mean: float
    pred_std: float
    
@app.get('/')
def home():
    return {'health_check': 'OK'}

@app.post('/prediction_mean_std', response_model=OutputPredParameters)
def get_pred_std(payload: InputFileParameters):
    try:
        
        pred_mean, pred_std = run_prediction(month=payload.month, year=payload.year)  
    except Exception as e:
        print('\tError message:', e, '\n')
        pred_mean = 0.0
        pred_std = 0.0
    return {'pred_mean': pred_mean, 'pred_std': pred_std}
