FROM python:3.8-slim

ADD api.py /

COPY ./requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

ENTRYPOINT ["python3"]

CMD ["api.py"]
