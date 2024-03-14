FROM python:3.10

WORKDIR /part1

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

CMD python src/main.py