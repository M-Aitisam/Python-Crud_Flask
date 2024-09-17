pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'flask-pyodbc-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = "${env.dockerHubUser}/flask-pyodbc-app:${DOCKER_TAG}"
        FLASK_PORT = '5000'
    }
    
    stages {
        stage("Clone Repository") {
            steps {
                echo "Clone code from GitHub"
                git url: "https://github.com/M-Aitisam/Python-Crud_Flask.git", branch: "master"
            }
        }
      
        stage("Build Docker Image") {
            steps {   
                echo "Building Docker image for the Flask app"
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }
        
        stage("Push Docker Image to Docker Hub") {
            steps {
                echo "Pushing image to Docker Hub"
                withCredentials([usernamePassword(credentialsId: "dockerHUb", passwordVariable: "dockerHubPass", usernameVariable: "dockerHubUser")]) {
                    sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_REGISTRY}"
                    sh "docker login -u ${dockerHubUser} -p ${dockerHubPass}"
                    sh "docker push ${DOCKER_REGISTRY}"
                }
            }
        }
        
        stage("Deploy Docker Container") {
            steps {
                echo "Deploy Docker container"
                sh """
                    docker stop flask-pyodbc-app || true
                    docker rm flask-pyodbc-app || true
                    docker run -d --name flask-pyodbc-app -p ${FLASK_PORT}:${FLASK_PORT} \
                    -e SQL_SERVER_DRIVER='{ODBC Driver 17 for SQL Server}' \
                    -e SQL_SERVER_HOST='localhost' \
                    -e SQL_SERVER_DATABASE='Python_Flask_Crud_db' \
                    -e SQL_SERVER_USERNAME='sa' \
                    -e SQL_SERVER_PASSWORD='aitisam24' \
                    ${DOCKER_REGISTRY}
                """
            }
        }
    }
    
    post {
        always {
            echo "Cleaning up unused Docker resources"
            sh "docker system prune -f"
        }
    }
}
