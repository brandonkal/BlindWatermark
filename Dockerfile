FROM python:3.8.5-slim
COPY --from=openjdk:16-slim / /
WORKDIR /app

RUN apt-get update && apt install \
  ffmpeg \
  libgl1-mesa-glx \
  python3-setuptools \
  libsm6 libxext6 -y --no-install-recommends && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV JAVA_HOME /usr/local/openjdk-16
ENV PATH $JAVA_HOME/bin:$PATH

COPY . .
RUN python ./download_jar.py && python setup.py install

ENTRYPOINT [ "python", "./bwm.py" ]