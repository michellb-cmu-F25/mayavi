pipeline {
    agent any
    
    tools {
        "hudson.plugins.sonar.SonarRunnerInstallation" "sonar-scanner"
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
