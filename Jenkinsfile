pipeline {
    agent any
    tools {
        nodejs 'newman'
    }

    // Read the config.json file and extract environment keys
    environment {
        CONFIG_FILE = 'config.json' 
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: getEnvironmentChoices(), description: 'Select the environment')
    }

    stages {
        // Step 1: Intro
        stage('Welcome') {
            steps {
                echo 'Welcome to APIM Automation'
            }
        }

        // Step 2: Execute hello.py
        stage('Run Hello Python Script') {
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

        // Step 3: Deploy
        stage('Run Newman') {
            steps {
                echo "Deploying to ${params.ENVIRONMENT} environment"
            }
        }

        // Step 4: Execution
        stage('Run API Testing') {
            steps {
                script {
                   sh "python3 api_test.py Sample ${params.ENVIRONMENT}"
                }
            }
        }
    }

    post {
        // Optional: Post-build actions
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
    def config = readJSON file: env.CONFIG_FILE

    // Extract keys from the env_mapping section
    def environments = config.env_mapping.keySet() as List

    // Return the list of environments
    return environments
}
