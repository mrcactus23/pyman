pipeline {
    agent any
    tools {
        nodejs 'newman'
    }
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['SIT', 'UAT', 'PRODUCTION'], description: 'Select the environment')
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

        stage('Stage 5: Jira Integration') {
            steps {
                script {
                    def testSuccess = sh(script: "python3 api_test.py ${params.ENDPOINT} ${params.ENVIRONMENT}", returnStatus: true) == 0
                    def summary = "API Test ${testSuccess ? 'Success' : 'Failure'} in ${params.ENVIRONMENT} for ${params.ENDPOINT}"
                    def description = "The API test automation ${testSuccess ? 'completed successfully' : 'failed'} in the ${params.ENVIRONMENT} environment for the ${params.ENDPOINT} endpoint."

                    def issueKey = sh(script: "python3 jira_utils.py create '${summary}' '${description}'", returnStdout: true).trim()
                    if (testSuccess) {
                        sh "python3 jira_utils.py update ${issueKey} 'Done'"
                    } else {
                        sh "python3 jira_utils.py update ${issueKey} 'To Do'"
                    }
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
