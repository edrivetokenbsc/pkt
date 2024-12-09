FROM python:latest
LABEL Maintainer="roushan.me17"
WORKDIR /usr/app/src
COPY os.py ./
CMD [ "python", "./os.py"]
