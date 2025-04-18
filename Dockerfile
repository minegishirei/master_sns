
# python version number:3.9.16
FROM python:3.9.16

# code ... directory for python codes.
WORKDIR /code

# copy localcode to container image.
COPY ./code /code

# upgrade pip command
RUN pip install --upgrade pip 

# install python lib 
RUN pip install -r requirements.txt

RUN apt-get update 
RUN apt-get install -y mecab \
  && apt-get install -y mecab-ipadic \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y swig
RUN pip install mecab-python3

ENV MECABRC /opt/homebrew/etc/mecabrc

ENV GROQ_API_KEY=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