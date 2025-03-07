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
                    // Run the test and capture the result
                    def testSuccess = sh(script: "python3 api_test.py ${params.ENDPOINT} ${params.ENVIRONMENT}", returnStatus: true) == 0
                    // Store the result in an environment variable for use in later stages
                    env.TEST_SUCCESS = testSuccess
                }
            }
        }

        stage('Stage 5: Jira Integration') {
            steps {
                script {
                    // Use the stored test result from Stage 4
                    def testSuccess = env.TEST_SUCCESS.toBoolean()
                    def summary = "API Test ${testSuccess ? 'Success' : 'Failure'} in ${params.ENVIRONMENT} for ${params.ENDPOINT}"
                    def description = "The API test automation ${testSuccess ? 'completed successfully' : 'failed'} in the ${params.ENVIRONMENT} environment for the ${params.ENDPOINT} endpoint."

                    // Create a Jira ticket and capture the issue key
                    echo 'Create a Jira ticket'
                    def issueKey = sh(script: "python3 jira_utils.py create_jira_ticket '${summary}' '${description}'", returnStdout: true).trim()

                    // Update the Jira ticket status based on the test result
                    echo 'Update the Jira ticket'
                    if (testSuccess) {
                        sh "python3 jira_utils.py update_jira_status ${issueKey} 'Done'"
                    } else {
                        sh "python3 jira_utils.py update_jira_status ${issueKey} 'To Do'"
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
