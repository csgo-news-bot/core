FROM python:3.8.7-slim

ARG PATH=/home/app
RUN ls -la
RUN mkdir -p ${PATH}
COPY . ${PATH}
WORKDIR ${PATH}

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["python", "main.py"]
