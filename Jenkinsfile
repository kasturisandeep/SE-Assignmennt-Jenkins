pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/kasturisandeep/SE-Assignmennt-Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x code.py"
                sh "./code.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
}
