FROM python:3

WORKDIR /sugano
COPY . .
RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
RUN sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
RUN chmod +x /usr/bin/geckodriver
RUN rm geckodriver-v0.23.0-linux64.tar.gz
RUN apt install firefox-esr -y

# ./scripts/run &
# python3 ./scripts/test.py
