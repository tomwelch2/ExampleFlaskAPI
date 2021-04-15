FROM python:3.8-slim

ADD setup.py /

COPY ./create_database.sql /

COPY ./create_table.sql /

COPY ./insert_data.sql /

RUN pip3 install sqlalchemy

RUN pip3 install pymysql

RUN pip3 install cryptography

ENTRYPOINT ["python3"]

CMD ["setup.py"]
