pipeline {
    agent any
    tools {
        nodejs 'newman' // Replace with the name of the Node.js installation in Jenkins
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

                    // Execute the Python script
                    sh 'python3 hello.py'
                }
            }
        }

        // Step 3: Install Newman
        stage('Run Newman') {
            steps {
                sh 'npm install newman --save-dev'
                sh 'newman -v'
            }
        }
        
        // Step 4: Execute api_test.py
        stage('Run API Testing') {
            steps {
                script {
                    sh 'python3 api_test.py Sample'
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
