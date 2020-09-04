FROM python:3.8

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python setup.py install

ENTRYPOINT [ "python", "./bwm.py" ]