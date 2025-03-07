pipeline {
    agent any
    tools {
        nodejs 'newman'
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['Dev', 'SIT', 'UAT'], description: 'Select the environment')
        choice(name: 'ENDPOINT', choices: ['Sample', 'AF', 'PF'], description: 'Select the endpoint')
    }

    stages {
        stage('Stage 1: Intro') {
            steps {
                echo 'Welcome to APIM Automation'
            }
        }

        stage('Stage 2: Installation') {
            steps {
                script {
                    // Ensure Python is installed
                    def pythonVersion = sh(script: 'python3 --version', returnStdout: true).trim()
                    echo "Using ${pythonVersion}"

                    // Install newman
                    sh 'npm install newman --save-dev'
                    sh 'newman -v'
                }
            }
        }

        stage('Stage 3: Deployment') {
            steps {
                echo "Deploying ${params.ENDPOINT} to ${params.ENVIRONMENT} environment"
            }
        }

        stage('Stage 4: Test Execution') {
            steps {
                script {
                   sh "python3 api_test.py ${params.ENDPOINT} ${params.ENVIRONMENT}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
