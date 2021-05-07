FROM node:latest

WORKDIR /app

ADD ./.env /app

ADD ./covid-19.json /app

ADD ./extract.js /app/extract.js

RUN npm install fs

RUN npm install mysql2

RUN npm install dotenv

RUN npm install system-sleep

ENTRYPOINT [ "node" ]

CMD ["/app/extract.js"]