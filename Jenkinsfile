pipeline {
    agent any

    environment {
        DEPLOY_SERVER = "ubuntu@52.66.240.91"
        APP_DIR = "/home/ubuntu/app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Pulling code from GitHub..."
                git branch: 'main',
                    url: 'git@github.com:subahvarma/my-ci-pipeline-demo-.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                sudo apt-get update -y
                sudo apt-get install -y python3-pip
                pip3 install -r requireents.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running unit tests..."
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy App') {
            steps {
                echo "Deploying app to EC2..."
                sh '''
                scp -o StrictHostKeyChecking=no -r * ${DEPLOY_SERVER}:${APP_DIR}/
                ssh -o StrictHostKeyChecking=no ${DEPLOY_SERVER} "nohup python3 ${APP_DIR}/app.py > app.log 2>&1 &"
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs.'
        }
    }
}

