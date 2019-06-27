FROM node:lts-alpine
WORKDIR /app
COPY dcbr-web/package*.json ./
RUN npm install
COPY dcbr-web/ .
RUN npm run build
