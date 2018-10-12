ARG PYTHON_VERSION=3.7
FROM python:alpine${PYTHON_VERSION}

ARG ROOT_APP=/project
ARG PORT=5000
ENV PORT=${PORT}

RUN apk update & apk add curl vim

LABEL mantainer=kr.rdz.20@gmail.com \
      version=1.0 \
      date=12-10-2018

RUN mkdir $ROOT_APP
WORKDIR $ROOT_APP

ADD requirements.txt $APP_ADD
RUN pip install -r requirements.txt

COPY . $ROOT_APP
EXPOSE $PORT

CMD gunicorn -w 4 -b 0.0.0.0:${PORT} app:app