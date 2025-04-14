pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = 'C:\\Users\\Amey S G\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Code cloned from GitHub automatically."
            }
        }

        stage('Set up Python Environment') {
            steps {
                bat '"%PYTHON%" -m venv %VENV_DIR%'
                bat 'call %VENV_DIR%\\Scripts\\activate.bat && "%PYTHON%" -m pip install --upgrade pip'
                bat 'call %VENV_DIR%\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat """
    call venv\\Scripts\\activate.bat
    python manage.py test --verbosity=2
"""

                
            }
        }
    }

    post {
        always {
            echo 'Test Pipeline Finished'
        }
        success {
            echo 'Tests Passed 🎉'
        }
        failure {
            echo 'Tests Failed ❌'
        }
    }
}
