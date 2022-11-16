## Create

```
docker build -t sample:1.0 .
```


#run
```
docker run sample:1.0

docker container run  sample:1.0  ping -c 5 8.8.8.8

#delete after running

docker run -it --rm  --name test sample:1.0
```

#run detatch
```
docker run -it --rm -d --name test sample:1.0
```


#vizualizare

```
docker ps

docker container ls

docker ps -a

docker container ls -a

```

## Inspect

```
docker container inspect test
```


#executa in container
```
docker container exec -it test /bin/sh
```


#attach to logs
```
docker container attach test
```


#retrive log

```
docker container --help

docker container logs --help

docker container logs  test

docker container logs --tail 5  test

docker container logs --tail 5  --follow test
```


#start/stop
```
docker container start random_trivia-container

docker container stop random_trivia-container

docker container rm random_trivia-container
```

## Image

```
docker image ls

docker image pull centos

docker image pull alpine

docker image pull alpine:3.5

#prepare for upload in repository

docker image tag myweb fredysa/myweb:1.0 

docker login

docker image push fredysa/myweb:1.0 
```

# Volume

```
docker volume create mydisk 

docker volume ls

docker volume inspect mydisk 

docker run --name mountsample -it --rm -v mydisk:/data alpine /bin/sh 
```

## add data to volume
```
cd /data
echo "some data" > sample.txt
exit
docker run --name mountsample -it --rm -v mydisk:/data ubuntu /bin/sh 
cd /data
ls
docker volume ls
docker volume inspect mydisk
docker volume rm mydisk
```

#share host volume

```
cd C:\Docker\_en\M-03\Example
docker image build -t my-website .
docker container run -d --rm --name my-site -p 8080:80 my-website
```

##PS 
```
docker container run -d --name my-site -v $pwd/src/:/usr/share/nginx/html -p 8080:80  my-website
```
##bash
```
docker container run -d --name my-site -v $(pwd):/usr/share/nginx/html -p 8080:80 my-website
```
# finish image for deploy

```
mkdir C:\Docker\_en\M-03\Example\finishversion

```
copy C:\Docker\_en\M-03\Example\src in C:\Docker\_en\M-03\Example\finishversion

copy docker file from C:\Docker\_en\M-03\Example\my-web in  C:\Docker\_en\M-03\Example\finishversion

```
cd C:\Docker\_en\M-03\Example\finishversion
docker image build -t my-website:1.0 .
docker container run -d --rm --name my-site2 -p 8081:80 my-website:1.0
docker image tag my-website:1.0 fredysa/my-website:2.0
docker login
docker image push fredysa/my-website:2.0
```
