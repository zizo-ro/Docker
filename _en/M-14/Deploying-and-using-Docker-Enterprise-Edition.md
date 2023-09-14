[![Home](../../img/home.png)](../M-14/README.md)
# Deploying  on AWS

## Setup User Permissions

- Connect to : https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users/details/demots?section=permissions
![aws](./img/access2.png)
![aws](./img/access1.png)

# Provisioning the infrastructure
In this first section, we are going to set up the infrastructure needed to install Docker UCP. This is relatively straightforward if you are somewhat familiar with AWS. Let's do this by following these steps:

- Create an **Auto Scaling group (ASG)** in AWS using the Ubuntu 16.04 server AMI. Configure the ASG to contain three instances of size **t2.xlarge**. Here is the result of this:

![aws](./img/l15-aws-p1.png)

ASG on AWS ready for Docker EE

- Once the ASG has been created, and before we continue, we need to open the **security group (SG)** a bit (which our ASG is part of) so that we can access it through SSH from our laptop and also so that the **virtual machines (VMs)** can communicate with each other.

- Navigate to your SG and add two new inbound rules, which are shown here:

![aws](./img/l15-aws-p2.png)

AWS SG settings

In the preceding screenshot, the first rule allows any traffic from my personal laptop (with the IP address **`70.113.114.234`**) to access any resource in the SG. The second rule allows any traffic inside the SG itself. These settings are not meant to be used in a production-like environment as they are way too permissive. However, for this demo environment, they work well.

Next, we will show you how to install Docker on the VMs we just prepared.

# Installing Docker
After having provisioned the cluster nodes, we need to install Docker on each of them. This can be easily achieved by following these steps:

- SSH into all three instances and install Docker. Using the downloaded key, SSH into the first machine:
```
$ ssh -i pets.pem ubuntu@<IP address>
```
Here, **`<IP address>`** is the public IP address of the VM we want to SSH into. 

- Now we can install Docker. For detailed instructions, refer to https://dockr.ly/2HiWfBc. We have a script in the**~/M-14/sample/aws** folder called install-docker.sh that we can use.

- First, we need to clone the labs GitHub repository to the VM:
```
git clone https://github.com/Fredy-SSA/DJK.git
cd ~/Lab-15-Coud/sample/aws
```

- Then, we run the script to install Docker:

```
 ./install-docker.sh
```
