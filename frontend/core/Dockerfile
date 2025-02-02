# Use Node.js for building the app
FROM node:20 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build -- --configuration production --project=core

# Use Nginx to serve the built Angular app
FROM nginx:alpine
COPY --from=build /app/dist/core/browser /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
