# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY dcbr-web/package*.json ./
RUN npm install
COPY dcbr-web/ .
RUN npm run build

# production stage
FROM abiosoft/caddy:1.0.0 as production-stage
COPY dcbr-web/openshift/config/Caddyfile /etc/Caddyfile
COPY --from=build-stage /app/dist /srv
