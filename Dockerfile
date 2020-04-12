FROM python:3.8

ENV APP /usr/src/app

RUN mkdir -p $APP
WORKDIR $APP

COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements.txt
ARG env
RUN if [ "$env" = "dev" ] ; then pip install -r requirements-dev.txt ; fi
