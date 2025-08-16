pipeline {
    agent any

    stages {
        stage('Clean Old Containers & Images') {
            steps {
                sh '''
                echo "Cleaning old containers..."
                docker ps -aq --filter "ancestor=todo-dev" | xargs -r docker rm -f
                docker rmi -f todo-dev || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                cd /home/ubuntu/projects/django-todo
                docker build -t todo-dev .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                echo "Running container..."
                docker run -d -p 8000:8000 todo-dev
                '''
            }
        }
    }

    post {
        success {
            echo "Build complete!"
        }
        failure {
            echo "Build failed!"
        }
    }
}

