FROM python:3.8.7-slim

ARG APP_PATH=/home/app
RUN mkdir -p ${APP_PATH}
COPY . ${APP_PATH}
WORKDIR ${APP_PATH}

RUN pip install pipenv

RUN apt update -yqq
RUN apt install wget curl unzip xvfb libxi6 libgconf-2-4 -yqq

# Install chromium
RUN apt install chromium -yqq
# Install chrome driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# Clean
RUN rm -f /tmp/chromedriver.zip

RUN pipenv install --deploy --system --ignore-pipfile
CMD ["python", "main.py"]
