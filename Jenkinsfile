<<<<<<< HEAD
pipeline {
    agent any

    environment {
        DOCKER_USER = "2023bcs0229shalini"
        ROLL = "2023bcs00229"

        FRONTEND_IMAGE = "${DOCKER_USER}/${ROLL}_frontend"
        BACKEND_IMAGE = "${DOCKER_USER}/${ROLL}_backend"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t $BACKEND_IMAGE ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t $FRONTEND_IMAGE ./frontend'
            }
        }

        stage('Push Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push $BACKEND_IMAGE
                    docker push $FRONTEND_IMAGE
                    docker logout
                    '''
                }
            }
        }
    }
=======
pipeline {
    agent any

    environment {
    DOCKER_USER = "2023bcs0229shalini"
    ROLL = "2023bcs00229"
    REG = "bcs229"

    FRONTEND_IMAGE = "${DOCKER_USER}/${REG}_${ROLL}_frontend"
    BACKEND_IMAGE = "${DOCKER_USER}/${REG}_${ROLL}_backend"
}

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t $BACKEND_IMAGE ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t $FRONTEND_IMAGE ./frontend'
            }
        }

        stage('Push Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push $BACKEND_IMAGE
                    docker push $FRONTEND_IMAGE
                    docker logout
                    '''
                }
            }
        }
    }
>>>>>>> d8f3121 (Initial project commit)
}