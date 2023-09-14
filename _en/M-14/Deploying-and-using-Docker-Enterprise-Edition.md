[![Home](../../img/home.png)](../M-14/README.md)
# Deploying  on AWS

## Setup User Permissions

- Connect to : https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users/details/demots?section=permissions
![aws](./img/access2.png)
![aws](./img/access1.png)

- Create access key (Download access key !)

- Add policy :
  ![aws](./img/access3.png)

For inline :
```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "eksadministrator",
			"Effect": "Allow",
			"Action": "eks:*",
			"Resource": "*"
		}
	]
}

```


### Download/Install  AWS CLI : https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

- Install Kubectl  
```
curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.4/2023-08-16/bin/windows/amd64/kubectl.exe
```
https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html


 ## Connect to CLI  
- Run :
```
aws configure

- Result:
AWS Access Key ID [****************QKXX]: AKIAR272E4Y5ADSDJGDGGDHD
AWS Secret Access Key [****************ZJcw]: H2y8zrRa71IgPM+6tAKCw4awert34t54twertw34t34
Default region name [None]:
Default output format [None]:

```




