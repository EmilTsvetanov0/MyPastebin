import torch
import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load('model.pkl')
tokenizer = joblib.load('tokenizer.pkl')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class TextInput(BaseModel):
    text: str

@app.post('/predict')
def predict(input: TextInput):
    inputs = tokenizer(input.text, return_tensors = "pt", truncation=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    prediction = model.config.id2label[logits.argmax().item()]
    return {"prediction": prediction}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=80)
