pipeline {
    agent any
    tools {
        nodejs 'newman'
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['SIT', 'UAT'], description: 'Select the environment')
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

                    // Install required Python packages
                    sh 'pip3 install -r requirements.txt'
                }
                // Install newman
                sh 'npm install newman --save-dev'
                sh 'newman -v'
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
                    // Run the API tests
                    sh "python3 api_test.py ${params.ENDPOINT} ${params.ENVIRONMENT}"
                }
            }
        }

        stage('Stage 5: Jira Integration') {
            steps {
                script {
                    // Update Jira based on test results
                    def testSuccess = sh(script: 'echo $?', returnStdout: true).trim() == '0'
                    if (testSuccess) {
                        echo '✅ Tests passed. Updating Jira...'
                        sh "python3 jira_integration.py ${params.ENDPOINT} ${params.ENVIRONMENT}"
                    /* groovylint-disable-next-line NestedBlockDepth */
                    } else {
                        echo '❌ Tests failed. Skipping Jira update.'
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
