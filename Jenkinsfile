pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = 'C:\\Users\\Amey S G\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning code from GitHub..."
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                bat '"%PYTHON%" -m venv %VENV_DIR%'
                bat 'call %VENV_DIR%\\Scripts\\activate.bat && "%PYTHON%" -m pip install --upgrade pip'
                bat 'call %VENV_DIR%\\Scripts\\activate.bat && pip install -r requirements.txt'
                bat 'call %VENV_DIR%\\Scripts\\activate.bat && pip freeze'
            }
        }

        stage('Apply Migrations') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python manage.py migrate
                """
            }
        }

        stage('Run All Tests') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python manage.py test --verbosity=2
                """
            }
        }

        stage('Run Navigation Test') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python manage.py test student.tests.test_navigation.NavigationTestCase --verbosity=2
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
