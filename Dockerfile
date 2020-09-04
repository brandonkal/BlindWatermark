FROM python:3.8

RUN apt-get update && apt-get install ffmpeg libgl1-mesa-glx \
  libsm6 libxext6  -y

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python setup.py install

ENTRYPOINT [ "python", "./bwm.py" ]