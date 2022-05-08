FROM python:3.7-slim

WORKDIR /knight_cab

COPY requirements.txt /knight_cab/
RUN pip install -r /knight_cab/requirements.txt
COPY . /knight_cab/

CMD python3 /knight_cab/bot.py
