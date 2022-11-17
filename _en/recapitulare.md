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

# create network

```
docker network --help
docker network create --help
docker network create --driver bridge Frontend-net
docker network create --driver bridge --subnet "10.2.0.0/16" Backend-net
```

#view newtork

```
docker network ls
docker network inspect  Frontend-net
docker network inspect  Backend-net
```
#test network settings

```
docker container run --name c1frontend -d --rm --network Frontend-net alpine:latest ping 127.0.0.1
docker container run --name c2all -d --rm --network Frontend-net alpine:latest ping 127.0.0.1
docker container run --name c3backend -d --rm --network Backend-net alpine:latest ping 127.0.0.1

docker network connect Backend-net c2all 

docker container exec -it c1frontend /bin/sh
docker container exec -it c2all  /bin/sh
docker container exec -it c3backend  /bin/sh
```

#clean up network

#sterge tot ce nu e folosit
```
docker network prune 
```
#sterge targetat
```
docker network  rm Backend-net
```

docker network ls



### Cleanup PS hystory
(Get-PSReadlineOption).HistorySavePath

delete C:\Users\srvuser6\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

