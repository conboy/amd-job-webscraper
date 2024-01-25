# curl -fsSL https://get.docker.com -o get-docker.sh
# sh get-docker.sh
# docker build -t fastapi . && docker run -d --name backend -p 80:80 fastapi

FROM python

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api.py /code

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]