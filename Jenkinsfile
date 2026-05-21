pipeline {

 agent any

 stages {

 stage('Install'){

 steps{

 sh 'pip install -r requirements.txt'

 }

 }

 stage('Test'){

 steps{

 sh 'pytest'

 }

 }

 stage('Docker Build'){

 steps{

 sh 'docker build -t ai-rag .'

 }

 }

 }

}