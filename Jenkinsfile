pipeline{
    agent any

    // tools {
    //      maven 'maven'
    //      jdk 'java'
    // }

    stages{
        stage('checkout'){
            steps{
                checkout([$class: 'GitSCM', 
                branches: [[name: '*/main']],  
                userRemoteConfigs: [[credentialsId: 'vsowmya26_itd', url: 'https://github.com/vsowmya26/my_repo.git']]])
            }
        }
        stage('build'){
            steps{
               sh 'mvn package'
            }
        }
        stage('test'){
            steps{
               sh 'mvn test'
            }
    }
}
