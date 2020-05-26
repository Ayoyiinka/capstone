pipeline {
    agent any
    stages {
    stage('Checking out git repo') {
      steps {
            sh 'echo "Checkout..."'
            checkout scm
      }
    }
    stage('Checking environment') {
      steps {
            sh 'echo "Checking environment..."'
            sh 'git --version'
            sh 'docker -v' 
      }
    }
    stage("Linting") {
      steps {
            sh 'echo "Linting..."'
      }
    }
    stage('Building image') {
      steps {
        	  sh 'echo "Building Docker image..."'
      }
    }
    stage('Deploying') {
      steps {
        sh 'echo "Deploying to AWS..."'
      }
    }
    stage("Cleaning up") {
      steps {
      sh 'echo "Cleaning up..."'
      sh "docker system prune"
        }
    }
}}
