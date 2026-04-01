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
                script {
                    def scannerHome = tool name: 'sonar-scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    sh """
                    ${scannerHome}/bin/sonar-scanner \
                      -Dsonar.projectKey=Mayavi-Analysis \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://sonarqube-service \
                      -Dsonar.login=\${SONAR_AUTH_TOKEN} \
                      -Dsonar.qualitygate.wait=true
                    """
                }
            }
        }

        stage('Run Hadoop MapReduce') {
            steps {
                script {
                    def bucketName = "michelle-cmu-hadoop-data"

                    sh "gsutil rm -rf gs://${bucketName}/repo-output/ || true"
                    sh "gsutil cp -r . gs://${bucketName}/repo-input/"

                    sh """
                    gcloud dataproc jobs submit pyspark line_count.py \
                        --cluster=hadoop-cluster-michelle \
                        --region=us-central1 \
                        -- gs://${bucketName}/repo-input/ gs://${bucketName}/repo-output/
                    """
                }
            }
        }
    }
}


