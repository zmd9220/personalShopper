# aws_deploy



## 1. 프로젝트 설치

```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).



## 2. AWS 배포 설정







## 3. Vue CLI 기반 배포법

- https://cli.vuejs.org/guide/deployment.html#docker-nginx 
- https://slog97.tistory.com/30 참고 하여 작성했음

1. 도커 설치 https://docs.docker.com/engine/install/ubuntu/
2. 프로젝트 메인 폴더에 Dockerfile 파일 생성

```dockerfile
# node 이미지를 받는다 build이미지이구나 
# node 기반의 이미지로 생성된다. 
FROM node:latest as build-stage 

# RUN, CMD, ENTRYPOINT의 명령이 실행될 디렉터리 
WORKDIR /app 

# package*.json이 WORKDIR에 복사된다 
COPY package*.json ./ 

# 복사했으니 디펜던시 설치가 가능하다 
RUN npm install 

# 소스코드를 복사한다 
COPY ./ . 

# build 해서 /dist 폴더에 빌드 파일이 생성된다. 
RUN npm run build 

# nginx 이미지를 받는다. 실행 이미지이구나 
FROM nginx as production-stage 

# app 디렉터리 생성 
RUN mkdir /app 

# builder에서 빌드한 바이너리를 실행할 이미지로 전달해주기 위해 copy --from 옵션을 사용하여 실행 이미지로 전달한다 
COPY --from=build-stage /app/dist /app 

# 작성한 nginx 설정파일을 복사한다. 
COPY nginx.conf /etc/nginx/nginx.conf 

# 변경된 설정을 잘 적용하기 위해 재시작한다. 
RUN service nginx restart 
```

