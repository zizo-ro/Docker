[![Home](../../img/home.png)](../M-01/README.md)

# The Linux command shell
Docker containers were first developed on Linux for Linux. It is hence natural that the primary command-line tool used to work with Docker, also called a shell, is a Unix shell; remember, Linux derives from Unix. Most developers use the Bash shell. On some lightweight Linux distributions, such as Alpine, Bash is not installed and consequently one has to use the simpler Bourne shell, just called sh. Whenever we are working in a Linux environment, such as inside a container or on a Linux VM, we will use either **/bin/bash** or **/bin/sh**, depending on their availability.

Although Apple's macOS X is not a Linux OS, Linux and macOS X are both flavors of Unix and hence support the same set of tools. Among those tools are the shells. So, when working on macOS, you will probably be using the Bash shell.

In this book, we expect from you a familiarity with the most basic scripting commands in Bash and PowerShell, if you are working on Windows. If you are an absolute beginner, then we strongly recommend that you familiarize yourself with the following cheat sheets:

- Linux Command Line Cheat Sheet by Dave Child at http://bit.ly/2mTQr8l
- PowerShell Basic Cheat Sheet at http://bit.ly/2EPHxze


# Docker - CLI Basic
### ! Do not Run on Powershell ISE !
### CLI or PS Interactive CMD

### Docker Help

```
docker image ls
docker container ls --all
docker --help
docker container --help
docker container ls --help
docker run --help
docker volume --help 
```

### Docker Run

```dockerfile
docker version
docker run hello-world
```
### Docker Build
```
docker build -t name .
docker push name
```

![cli](../../img/M-01/cli-cheat.png)