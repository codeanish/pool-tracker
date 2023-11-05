FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json .
COPY package-lock.json .

RUN npm install --silent
RUN npm install react-scripts -g --silent
COPY . ./

RUN npm run build

FROM nginx:alpine
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
WORKDIR /usr/share/nginx/html
RUN rm -rf *

COPY --from=builder /app/dist .
ENTRYPOINT ["nginx", "-g", "daemon off;"]