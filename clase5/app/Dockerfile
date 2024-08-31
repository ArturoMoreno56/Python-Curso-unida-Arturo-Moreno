FROM python:3.9

WORKDIR /APP

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["python","MAIN.PY"]