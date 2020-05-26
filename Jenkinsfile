pipeline {
    agent any
    stages {
    stage('Checking out git repo') {
      echo 'Checkout...'
      checkout scm
    }
    stage('Checking environment') {
      echo 'Checking environment...'
      sh 'git --version'
      echo "Branch: ${env.BRANCH_NAME}"
      sh 'docker -v'
    }
    stage("Linting") {
      echo 'Linting...'
      sh '/home/ubuntu/.local/bin/hadolint Dockerfile'
    }
    stage('Building image') {
	    echo 'Building Docker image...'
      withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
	     	sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
	     	sh "docker build -t 164678/udacity-capstone-project ."
	     	sh "docker tag 164678/udacity-capstone-project 164678/udacity-capstone-project"
	     	sh "docker push 164678/udacity-capstone-project"
      }
    }
    stage('Deploying') {
      echo 'Deploying to AWS...'
      dir ('./') {
        withAWS(credentials: 'aws-credentials', region: 'eu-central-1') {
            sh "aws eks --region eu-central-1 update-kubeconfig --name CapstoneEKS-VUUZkwHTDVPa"
            sh "kubectl apply -f aws/aws-auth-cm.yaml"
            sh "kubectl set image deployments/capstone-app capstone-app=164678/udacity-capstone-project:latest"
            sh "kubectl apply -f aws/capstone-app-deployment.yml"
            sh "kubectl get nodes"
            sh "kubectl get pods"
            sh "aws cloudformation update-stack --stack-name udacity-capstone-nodes --template-body file://aws/worker_nodes.yml --parameters file://aws/worker_nodes_parameters.json --capabilities CAPABILITY_IAM"
        }
      }
    }
    stage("Cleaning up") {
      echo 'Cleaning up...'
      sh "docker system prune"
      }
    }
}
