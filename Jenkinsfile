pipeline {
    agent any  // Run on any available agent

    stages {
        // Step 1: Print "Welcome"
        stage('Welcome') {
            steps {
                echo 'Welcome'
            }
        }

        // Step 2: Execute main.py
        stage('Run Python Script') {
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