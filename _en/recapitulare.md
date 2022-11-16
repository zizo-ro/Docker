# Image

docker image ls

docker image pull centos

docker image pull alpine

docker image pull alpine:3.5

#prepare for upload in repository

docker image tag myweb fredysa/myweb:1.0 

docker login

docker image push fredysa/myweb:1.0 

# Volume

docker volume create mydisk 

docker volume ls

docker volume inspect mydisk 

docker run --name mountsample -it --rm -v mydisk:/data alpine /bin/sh 

## add data to volume

cd /data

echo "some data" > sample.txt

exit

docker run --name mountsample -it --rm -v mydisk:/data ubuntu /bin/sh 

cd /data

ls

docker volume ls

docker volume inspect mydisk

docker volume rm mydisk

#share host volume

C:\Docker\_en\M-03\Example

docker image build -t my-website .

docker container run -d --rm --name my-site -p 8080:80 my-website

##PS 

docker container run -d --name my-site -v $pwd/src/:/usr/share/nginx/html -p 8080:80  my-website

##bash
docker container run -d --name my-site -v $(pwd):/usr/share/nginx/html -p 8080:80 my-website

# finish image for deploy

cd C:\Docker\_en\M-03\Example\finishversion

docker image build -t my-website:1.0 .

docker container run -d --rm --name my-site2 -p 8081:80 my-website:1.0

docker image tag my-website:1.0 fredysa/my-website:2.0

docker login

docker image push fredysa/my-website:2.0

