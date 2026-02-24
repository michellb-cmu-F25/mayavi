pipeline {
    agent any
    
    tools {
        "sonar-scanner" "sonar-scanner"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=Mayavi-Analysis -Dsonar.sources=.'
                }
            }
        }
        
        stage('Deploy Prep') {
            steps {
                echo 'Analysis complete. Ready for Dataproc deployment steps!'
            }
        }
    }
}
