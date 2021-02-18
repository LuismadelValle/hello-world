FROM python:3.8-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /

CMD ["python", "go_Luisma2.py"]
