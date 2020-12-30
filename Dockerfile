FROM python:3.8.7-slim

ARG PATH=/home/app
RUN ls -la
RUN mkdir -p ${PATH}
COPY . ${PATH}
WORKDIR ${PATH}

RUN pip install pipenv
RUN ls -la
RUN pipenv install
CMD ["python", "main.py"]
