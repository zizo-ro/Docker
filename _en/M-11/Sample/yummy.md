# Yummy project

1- download web project 

###    copy projet in folder Yummy 
    
2- Create Docker file

```
FROM nginx:latest
COPY ./Yummy /usr/share/nginx/html
```

3- Build docker 

```
docker build -t fredysa/papa:1.0 .
```

4- Test image

```
docker run -p 80:80 --rm --name yummy fredysa/papa:1.0
```

5- Uploat to repository
```
docker login
docker push fredysa/papa:1.0
```

6- Create  kubernet yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: yummy 
spec:
  replicas: 2
  selector:
    matchLabels:
      app: yummy
      service: yummy
  template:
    metadata:
      labels:
        app: yummy
        service: yummy
    spec:
      containers:
      - image: fredysa/papa:1.0
        name: yummy
        ports:
        - containerPort: 80
          protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: yummy
spec:
  type: NodePort
  ports:
  - port: 80
    protocol: TCP
  selector:
    app: yummy
    service: yummy
```

7- save as yummy.yaml 

8- run yaml 

```
    kubectl create -f .\yummy.yaml
    kubectl get all
```
