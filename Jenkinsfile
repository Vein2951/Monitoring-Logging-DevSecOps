pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Dependency Security Scan') {
            steps {
                sh 'pip-audit -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t lab3-flask:1.0 .'
            }
        }

        stage('Docker Image Security Scan') {
            steps {
                sh 'trivy image --exit-code 1 --severity HIGH,CRITICAL lab3-flask:1.0'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Security checks passed. Application is ready for deployment.'
            }
        }
    }
}
