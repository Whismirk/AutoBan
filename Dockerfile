# Deriving the latest base image
FROM python:latest

# Labels as key value pair
LABEL Maintainer="Rikj000"

# Any working direcrtory can be chosen as per choice like '/' or '/home' etc, I have chosen /usr/app/src
WORKDIR /usr/app/src

# Copy files from the working directory into the container
COPY autoban.py ./
COPY requirements.txt ./

# Install the requirements & run the Auto-Ban Bot
RUN pip install -r requirements.txt
CMD [ "python", "./autoban.py"]