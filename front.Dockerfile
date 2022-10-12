FROM node:12.18.1

WORKDIR /app

ENV NODE_ENV=production

COPY front.html index.html

RUN npm install http-server -g

CMD [ "http-server" ]