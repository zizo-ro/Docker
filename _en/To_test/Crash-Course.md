# Busybox 


```dos
docker run busybox:1.24 echo "hello world"
```
**echo "hello world"** is the command that we want to run on our container, see the next example

```dos
docker run busybox:1.24 ls /
```

# Run in the interactive way 

```dotnetcli
docker run -i -t  busybox 

ls -lah
...

exit
```

alternative run is 

```
docker run -it  busybox 


```

