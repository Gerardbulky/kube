FROM python:3.9-slim-buster
WORKDIR /kube-flask
COPY ./requirements.txt /kube-flask/
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]