FROM python:alpine3.18

WORKDIR /app

ADD . /app

RUN pip install flask

ENTRYPOINT ["python"]

CMD ["my-app.py"]