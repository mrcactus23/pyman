pipeline {
    agent any
    tools {
        nodejs 'newman'
    }
    // Define the path to the config.json file
    environment {
        CONFIG_FILE = 'config.json' // Path to your config.json file
    }

    // Read the config.json file and populate parameters
    parameters {
        choice(name: 'ENVIRONMENT', choices: [], description: 'Select the environment')
        choice(name: 'ENDPOINT', choices: [], description: 'Select the endpoint')
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

        stage('Initialize Parameters') {
            steps {
                script {
                    // Read the config.json file and populate parameters
                    def config = readConfigFile()
                    env.ENVIRONMENT_CHOICES = config.env_mapping.keySet().join('\n')
                    env.ENDPOINT_CHOICES = config.collections.keySet().join('\n')
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

// Function to read and parse the config.json file
def readConfigFile() {
    // Read the file content
    def configText = readFile(env.CONFIG_FILE)

    // Parse the JSON content using Groovy's JsonSlurper
    def config = new groovy.json.JsonSlurper().parseText(configText)

    // Return the parsed JSON object
    return config
}
