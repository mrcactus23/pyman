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
        choice(name: 'ENVIRONMENT', choices: getEnvironmentChoices(), description: 'Select the environment')
        choice(name: 'ENDPOINT', choices: getEndpointChoices(), description: 'Select the endpoint')
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

// Function to read config.json and extract environment keys
def getEnvironmentChoices() {
    // Read the config.json file
    def config = readConfigFile()

    // Extract keys from the env_mapping section
    def environments = config.env_mapping.keySet() as List

    // Return the list of environments
    return environments
}

// Function to read config.json and extract endpoint keys
def getEndpointChoices() {
    // Read the config.json file
    def config = readConfigFile()

    // Extract keys from the collections section
    def endpoints = config.collections.keySet() as List

    // Return the list of endpoints
    return endpoints
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
