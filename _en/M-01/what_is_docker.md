[![Home](../../img/home.png)](../README.md)

# What is Docker ?

:::image type="content" source="../../img/d_emdyhfmttad.jpg" alt-text="img":::

- [What are containers?](#what-are-containers-and-why-should-i-use-them)
- [Why are containers important?](#why-are-containers-important)
- The Moby project]
- [Docker products]
- [Container architecture]


# What Are Containers and Why Should I Use Them?

This first chapter will introduce you to the world of containers and their orchestration. This book starts from the very beginning, in that it assumes that you have no prior knowledge of containers, and will give you a very practical introduction to the topic.

In this chapter, we will focus on the software supply chain and the friction within it. Then, we'll present containers, which are used to reduce this friction and add enterprise-grade security on top of it. We'll also look into how containers and the ecosystem around them are assembled. We'll specifically point out the distinction between the upstream **Open Source Software (OSS)** components, united under the code name [Moby](https://mobyproject.org/), that form the building blocks of the downstream products of Docker and other vendors.

**Docker**, a subset of the Moby project, is a software framework for building, running, and managing containers on servers and the cloud. The term "docker" may refer to either the tools (the commands and a daemon) or to the Dockerfile file format.



### Alternatives to Docker
Linux containers have facilitated a massive shift in high-availability computing. There are many toolsets out there to help you run services, or even your entire operating system, in containers. The **Open Container Initiative (OCI)** is an industry standards organization that encourages innovation while avoiding the danger of vendor lock-in. Thanks to the OCI, you have a choice when choosing a container toolchain, including **Docker**, **CRI-O**, **Podman**, **LXC**, and others.


# Why are containers important?

:::image type="content" source="../../img/d_wfip.jpg" alt-text="Img":::

### Before Docker containers
For many years now, enterprise software has typically been deployed either on “bare metal” (i.e. installed on an operating system that has complete control over the underlying hardware) or in a virtual machine (i.e. installed on an operating system that shares the underlying hardware with other “guest” operating systems). Naturally, installing on bare metal made the software painfully difficult to move around and difficult to update—two constraints that made it hard for IT to respond nimbly to changes in business needs.

Then virtualization came along. Virtualization platforms (also known as “hypervisors”) allowed multiple virtual machines to share a single physical system, each virtual machine emulating the behavior of an entire system, complete with its own operating system, storage, and I/O, in an isolated fashion. IT could now respond more effectively to changes in business requirements, because VMs could be cloned, copied, migrated, and spun up or down to meet demand or conserve resources.

Virtual machines also helped cut costs, because more VMs could be consolidated onto fewer physical machines. Legacy systems running older applications could be turned into VMs and physically decommissioned to save even more money.

But virtual machines still have their share of problems. Virtual machines are large (gigabytes), each one containing a full operating system. Only so many virtualized apps can be consolidated onto a single system. Provisioning a VM still takes a fair amount of time. Finally, the portability of VMs is limited. After a certain point, VMs are not able to deliver the kind of speed, agility, and savings that fast-moving businesses are demanding.

### Docker container benefits
Containers work a little like VMs, but in a far more specific and granular way. They isolate a single application and its dependencies—all of the external software libraries the app requires to run—both from the underlying operating system and from other containers. All of the containerized apps share a single, common operating system (either Linux or Windows), but they are compartmentalized from one another and from the system at large.

### The benefits of Docker containers show up in many places. Here are some of the major advantages of Docker and containers:

Docker enables more efficient use of system resources
Instances of containerized apps use far less memory than virtual machines, they start up and stop more quickly, and they can be packed far more densely on their host hardware. All of this amounts to less spending on IT.

The cost savings will vary depending on what apps are in play and how resource-intensive they may be, but containers invariably work out as more efficient than VMs. It’s also possible to save on costs of software licenses, because you need many fewer operating system instances to run the same workloads.

### Docker enables faster software delivery cycles
Enterprise software must respond quickly to changing conditions. That means both easy scaling to meet demand and easy updating to add new features as the business requires. 

Docker containers make it easy to put new versions of software, with new business features, into production quickly—and to quickly roll back to a previous version if you need to. They also make it easier to implement strategies like blue/green deployments.

### Docker enables application portability
Where you run an enterprise application matters—behind the firewall, for the sake of keeping things close by and secure; or out in a public cloud, for easy public access and high elasticity of resources. Because Docker containers encapsulate everything an application needs to run (and only those things), they allow applications to be shuttled easily between environments. Any host with the Docker runtime installed—be it a developer’s laptop or a public cloud instance—can run a Docker container.

### Docker shines for microservices architecture
Lightweight, portable, and self-contained, Docker containers make it easier to build software along forward-thinking lines, so that you’re not trying to solve tomorrow’s problems with yesterday’s development methods.

One of the software patterns containers make easier is microservices, where applications are constituted from many loosely coupled components. By decomposing traditional, “monolithic” applications into separate services, microservices allow the different parts of a line-of-business app to be scaled, modified, and serviced separately—by separate teams and on separate timelines, if that suits the needs of the business. 

Containers aren’t required to implement microservices, but they are perfectly suited to the microservices approach and to agile development processes generally.



# Links 

- Docker overview: https://docs.docker.com/engine/docker-overview/
- The Moby project: https://mobyproject.org/
- Docker products: https://www.docker.com/get-started
- Cloud-Native Computing Foundation: https://www.cncf.io/ (Free Trainings)
- containerd – an industry-standard container runtime: https://containerd.io/