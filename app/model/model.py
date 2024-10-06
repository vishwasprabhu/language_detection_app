import pickle
import re
import mlflow
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent
MLFLOW_RUN_ID = '1e9fb8e091714130b07ac2b9644fa17b'

# Load the model from MLflow
# mlflow_model_path = f'runs:/{MLFLOW_RUN_ID}/language_detection_model'
mlflow_model_path = f'{BASE_DIR}/mlruns/{MLFLOW_RUN_ID}/artifacts/language_detection_model'  
model = mlflow.pyfunc.load_model(mlflow_model_path)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return pred[0]