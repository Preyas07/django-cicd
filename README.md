
# django-todo
A simple todo app built with django

![todo App](https://raw.githubusercontent.com/shreys7/django-todo/develop/staticfiles/todoApp.png)
### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
$ git clone https://github.com/shreys7/django-todo.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
$ python manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
$ python manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/todos for the App.

Cheers and Happy Coding :)

# Run with Docker

Build and run the app using Docker:

```bash
docker build -t todo-dev .
docker run -d -p 8000:8000 todo-dev
```

App will be available at 👉 http://localhost:8000

CI/CD with Jenkins

## This repository includes a Jenkinsfile that automates:

Clean up old containers and images

Build a fresh Docker image

Deploy a new container on port 8000

# Jenkinsfile (excerpt)
```bash
pipeline {
    agent any

    stages {
        stage('Clean Old Containers & Images') {
            steps {
                sh '''
                docker ps -aq --filter "ancestor=todo-dev" | xargs -r docker rm -f
                docker rmi -f todo-dev || true
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                cd /home/ubuntu/projects/django-todo
                docker build -t todo-dev .
                '''
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 todo-dev'
            }
        }
    }

    post {
        success {
            echo "✅ Build complete!"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}

```
### Jenkins Dashboard
This shows the list of jobs and their statuses.

![Jenkins Dashboard](https://raw.githubusercontent.com/Preyas07/django-cicd/main/static/Jenkins-dashboard.png)

### Jenkins Build Logs
This shows the detailed console output of a successful build.

![Jenkins Build Logs](https://raw.githubusercontent.com/Preyas07/django-cicd/main/static/Jenkins-logs.png)

(Save your Jenkins success screenshot in the repo as jenkins-success.png so it displays here.)

## Tech Stack

Python 3.11

Django 3.2

Docker

Jenkins

Cheers and Happy CI/CD 🚀

