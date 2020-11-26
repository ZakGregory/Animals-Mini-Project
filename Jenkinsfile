pipeline{
        agent any
        stages{
            stage('Build Images'){
                steps{
                    sh "sudo docker-compose build"
                }
            }
            stage('Deploy'){
                steps{
		    sh "docker stack deploy --compose-file docker-compose.yml animal-app"
                }
            }
        }    
}

