pipeline{
        agent any
        stages{
            stage('Build Images'){
                steps{
                    sh "sudo docker-compose build"
                }
            }
            stage('Test'){
                steps{
		}
	    }
            stage('Deploy'){
                steps{
		    sh "docker stack deploy --compose-file docker-compose.yml animal-app"
                }
            }
        }    
}

