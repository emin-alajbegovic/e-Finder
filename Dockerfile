# image
FROM python:3.8-slim-buster

# copy all files from current directory into the image
COPY . .

# already enabled in python - os library
# RUN pip install os-sys

# command to run it
CMD [ "python", "./main.py" ]