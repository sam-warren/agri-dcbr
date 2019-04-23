# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY dcbr-web/package*.json ./
RUN npm install
COPY dcbr-web/ .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]