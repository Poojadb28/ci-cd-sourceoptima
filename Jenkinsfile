pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version
                "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install --upgrade pip
                "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt
                """
            }
        }

        stage('Prepare Folders') {
            steps {
                bat "if not exist reports mkdir reports"
            }
        }

        stage('Run Tests') {
            steps {
                bat "\"C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe\" -m pytest tests/test_e2e_flow.py -v --html=reports/report.html"
            }
        }
    }

    post {
        always {
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test Report',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])
        }
    }
}

// pipeline {
//     agent any

//     stages {

//         stage('Checkout Code') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 // bat '"C:\\Users\\pooja.db\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
//                 bat '"C:\\Users\\Dell\\Downloads\\python-3.13.13-amd64\\python.exe" -m pytest -n auto --html=reports/report.html'
//             }
//         }

//         stage('Prepare Folders') {
//             steps {
//                 bat "if not exist reports mkdir reports"
//                 bat "if not exist screenshots mkdir screenshots"
//                 bat "if not exist downloads mkdir downloads"
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 // bat '"C:\\Users\\pooja.db\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest -n auto --html=reports/report.html'
//                 bat '"C:\\Users\\Dell\\Downloads\\python-3.13.13-amd64\\python.exe" -m pytest -n auto --html=reports/report.html'
//             }
//         }
//     }

//     post {
//         always {
//             publishHTML(target: [
//                 reportDir: 'reports',
//                 reportFiles: 'report.html',
//                 reportName: 'Test Report',
//                 keepAll: true,
//                 alwaysLinkToLastBuild: true,
//                 allowMissing: true
//             ])
//         }
//     }
// }

// pipeline {
//     agent any

//     environment {
//         PYTHON = "python"
//     }

//     stages {

//         stage('Checkout Code') {
//             steps {
//                 git url: 'https://github.com/Poojadb28/demo_sourceoptima', branch: 'main'
//             }
//         }

//           stage('Check Python') {
//             steps {
//                 bat "where python"
//                 bat "python --version"
//             }
//         }


//         stage('Setup Python') {
//             steps {
//                 bat "${PYTHON} --version"
//                 bat "pip install --upgrade pip"
//             }
//         }
      
//         stage('Install Dependencies') {
//             steps {
//                 bat "pip install -r requirements.txt"
//             }
//         }

//         stage('Prepare Folders') {
//             steps {
//                 bat "mkdir reports"
//                 bat "mkdir screenshots"
//                 bat "mkdir downloads"
//             }
//         }

//         stage('Run Smoke Tests') {
//             steps {
//                 bat "pytest -m smoke -n auto --html=reports/smoke_report.html"
//             }
//         }

//         stage('Run Regression Tests') {
//             steps {
//                 bat "pytest -m regression -n auto --html=reports/regression_report.html"
//             }
//         }
//     }

//     post {

//         always {
//             archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
//             archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
//             archiveArtifacts artifacts: 'downloads/*', allowEmptyArchive: true
//         }

//         success {
//             echo "Build Passed - All tests successful"
//         }

//         failure {
//             echo "Build Failed - Check reports"
//         }
//     }
// }