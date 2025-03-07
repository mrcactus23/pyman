pipeline {
    agent any
    tools {
        nodejs 'newman'
    }
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['SIT', 'UAT', 'PRODUCTION'], description: 'Select the environment')
        choice(name: 'ENDPOINT', choices: ['Sample', 'AF', 'PF'], description: 'Select the endpoint')
        string(name: 'JIRA_SUMMARY', defaultValue: '', description: 'Custom Jira ticket summary')
        string(name: 'JIRA_DESCRIPTION', defaultValue: '', description: 'Custom Jira ticket description')
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

                    // Install Python dependencies
                    sh 'pip3 install jira'
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

                    // Define summary and description
                    def summary = params.JIRA_SUMMARY ?: "API Test ${testSuccess ? 'Success' : 'Failure'} in ${params.ENVIRONMENT} for ${params.ENDPOINT}"
                    def description = params.JIRA_DESCRIPTION ?: "The API test automation ${testSuccess ? 'completed successfully' : 'failed'} in the ${params.ENVIRONMENT} environment for the ${params.ENDPOINT} endpoint."

                    // Create a Jira ticket and capture the issue key
                    echo 'Creating a Jira ticket...'
                    def issueKey = sh(script: "python3 jira_utils.py create '${summary}' '${description}' 2>/dev/null", returnStdout: true).trim()
                    echo "!!!Created Jira ticket: ${issueKey}!!!"

                    // Verify the issueKey is not empty
                    if (issueKey == null || issueKey.isEmpty()) {
                        error("Failed to create Jira ticket: issueKey is empty or null")
                    }

                    // Update the Jira ticket status based on the test result
                    echo 'Updating the Jira ticket...'
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
