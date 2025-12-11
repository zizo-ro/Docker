[![Home](../../img/home.png)](../M-11/README.md)
# Introduction to Docker Kubernets

## Install Kubernets

![m12](./img/k1.png)

##

![m12](./img/k2.png)

##
![m12](./img/k3.png)

##

![m12](./img/k4.png)
## 
![m12](./img/k5.png)

Let's make sure that Kubernetsis running with the following command:

```
kubectl get all
kubectl get nodes
```

# Instalare Kubernetes Dashboard

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

## Creaza user temporar :

```
kubectl create serviceaccount dashboard-admin-san -n kubernetes-dashboard
kubectl create clusterrolebinding dashboard-admin-san --clusterrole=cluster-admin --serviceaccount=kubernetes-dashboard:dashboard-admin-san
```

## Creează un token pentru autentificare (exemplu pentru un user admin temporar):

```
kubectl create token dashboard-admin-sa -n kubernetes-dashboard
```

##  Pornește accesul local:

```
kubectl proxy
```

##  Accesează:
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/



