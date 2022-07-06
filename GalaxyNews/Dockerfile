FROM python:3.8
ENV mkdir /galaxynews
RUN mkdir /galaxynews
WORKDIR /galaxynews
ADD requirements.txt /galaxynews/
RUN pip install -r requirements.txt
ADD . /galaxynews/

