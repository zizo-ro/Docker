https://docs.docker.com/samples/django/

# Define the project components

For this project, you need to create a Dockerfile, a Python dependencies file, and a docker-compose.yml file. (You can use either a .yml or .yaml extension for this file.)

    Create an empty project directory.

    You can name the directory something easy for you to remember. This directory is the context for your application image. The directory should only contain resources to build that image.

    Create a new file called Dockerfile in your project directory.

    The Dockerfile defines an application’s image content via one or more build commands that configure that image. Once built, you can run the image in a container. For more information on Dockerfile, see the Docker user guide and the Dockerfile reference.

    Add the following content to the Dockerfile.


```dockerfile
# syntax=docker/dockerfile:1
    FROM python:3
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    WORKDIR /code
    COPY requirements.txt /code/
    RUN pip install -r requirements.txt
    COPY . /code/
```

    This Dockerfile starts with a Python 3 parent image. The parent image is modified by adding a new code directory. The parent image is further modified by installing the Python requirements defined in the requirements.txt file.

    Save and close the Dockerfile.

    Create a requirements.txt in your project directory.

    This file is used by the **RUN pip install -r requirements.txt** command in your Dockerfile.

    Add the required software in the file.

```python
    Django>=3.0,<4.0
    psycopg2>=2.8
```

    Save and close the requirements.txt file.

    Create a file called **docker-compose.yml** in your project directory.

    The docker-compose.yml file describes the services that make your app. In this example those services are a web server and database. The compose file also describes which Docker images these services use, how they link together, any volumes they might need to be mounted inside the containers. Finally, the docker-compose.yml file describes which ports these services expose. See the docker-compose.yml reference for more information on how this file works.

    Add the following configuration to the file.


```yml
version: "3.9"
       
    services:
      db:
        image: postgres
        volumes:
          - ./data/db:/var/lib/postgresql/data
      web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
          - .:/code
        ports:
          - "8000:8000"
        environment:
          - POSTGRES_NAME=postgres
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=postgres
        depends_on:
          - db
```

    This file defines two services: The db service and the web service.

        Note:

        This uses the build in development server to run your application on port 8000. Do not use this in a production environment. For more information, see Django documentation.

    Save and close the docker-compose.yml file.

Create a Django project

In this step, you create a Django starter project by building the image from the build context defined in the previous procedure.

    Change to the root of your project directory.

    Create the Django project by running the docker-compose run command as follows.

```dockerfile
docker-compose run web django-admin startproject my_app .
```

This instructs Compose to run django-admin startproject composeexample in a container, using the web service’s image and configuration. Because the web image doesn’t exist yet, Compose builds it from the current directory, as specified by the build: . line in docker-compose.yml.

Once the web service image is built, Compose runs it and executes the django-admin startproject command in the container. This command instructs Django to create a set of files and directories representing a Django project.

After the docker-compose command completes, list the contents of your project.

```dos
ls -l
```

If you are running Docker on Linux, the files django-admin created are owned by root. This happens because the container runs as the root user. Change the ownership of the new files.

```dos
sudo chown -R $USER:$USER .
```

If you are running Docker on Mac or Windows, you should already have ownership of all files, including those generated by django-admin. List the files just to verify this.

```dos
ls -l
```

## Connect the database

In this section, you set up the database connection for Django.

    In your project directory, edit the composeexample/settings.py file.

    Replace the DATABASES = ... with the following:

    # settings.py
       
  
```python
import os
       
    [...]
       
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': 5432,
        }
    }
```

    These settings are determined by the postgres Docker image specified in docker-compose.yml.

    Save and close the file.

    Run the docker-compose up command from the top level directory for your project.

 docker-compose up

At this point, your Django app should be running at port 8000 on your Docker host. On Docker Desktop for Mac and Docker Desktop for Windows, go to http://localhost:8000 on a web browser to see the Django welcome page.