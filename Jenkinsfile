pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Build and Deploy') {
            steps {
                sh '''
                    docker compose down || true
                    docker compose pull
                    docker compose up -d
                '''
            }
        }
    }
}
