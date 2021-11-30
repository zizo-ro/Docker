[![Home](../../../../img/home.png)](../../../../README.md)

## Python random Jockes

Move to folder :

**cd ...\M-02\Example\11_Python_Random_Trivia**

## Build Images 

```dockerfile
docker build -t random_trivia .
```

## Run Container

- Run container in current terminal
```dos
docker container run --rm -it --name app  random_trivia
```
- Run container in a detached terminal

```dos
docker container run --rm -it -d --name app  random_trivia
```

