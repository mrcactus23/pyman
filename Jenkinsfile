pipeline {
    agent any  // Run on any available agent

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

                    // Execute the Python script
                    sh 'python3 hello.py'
                }
            }
        }

        // Step 3: Execute api_test.py
        stage('Run API Testing') {
            steps {
                script {
                    sh 'python3 api_test.py'
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