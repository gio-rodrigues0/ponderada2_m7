FROM python:latest

WORKDIR /work

COPY . .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]