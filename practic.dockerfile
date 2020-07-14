FROM python:3.6-slim
LABEL maintainer="nvworkacc@gmail.com"
ADD * /app/
WORKDIR /app
RUN pip install -r requirments.txt
RUN jupyter-nbconvert --execute practic.ipynb