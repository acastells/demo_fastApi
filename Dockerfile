FROM python:3.11.8-alpine3.19

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./api.py /app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0"]