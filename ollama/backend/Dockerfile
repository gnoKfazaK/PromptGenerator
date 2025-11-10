FROM python:3.12

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY FastAPI.py promptGeneration.py prompt.txt ./

CMD ["uvicorn", "FastAPI:app", "--host", "0.0.0.0", "--port", "8000"]