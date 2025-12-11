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

## Verify that Kubernetes is Running

```
kubectl get allkubectl get nodesShow more lines
```
Install Kubernetes Dashboard

## Create a Temporary Admin User

```
kubectl create serviceaccount dashboard-admin-sa -n kubernetes-dashboardShow more lines
```

## Generate an Authentication Token (for the temporary admin user)

```
kubectl create token dashboard-admin-sa -n kubernetes-dashboardShow more lines
```

## Start Local Access (Proxy)

```
kubectl proxyShow more lines
```

## Access the Dashboard

Open the following URL in your browser:
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/


