pipeline{
        agent any
        environment {
            DATABASE_URI = credentials('DATABASE_URI')
            docker_password = credentials('docker_password')
            app_version = 'v1'
        }
        stages{
            stage('Build Container'){
                steps{
                    sh "sudo docker-compose build"
                }
            }
            stage('Testing the Application'){
                steps{
                    sh "pip3 install -r requirements.txt"
                    sh "python3 -m pytest ./number_api --cov=app"
                    sh "python3 -m pytest ./word_api --cov=app"
                    sh "python3 -m pytest ./prompt_api --cov=app"
                    sh "python3 -m pytest ./server --cov=app"
                    
                }
            }
            stage('Push Containers'){
                steps{
                    sh 'docker login -u hgwright -p ${docker_password}'
                    sh 'docker push hgwright/challenge_server:${app_version}'
                    sh 'docker push hgwright/challenge_number_api:${app_version}'
                    sh 'docker push hgwright/challenge_word_api:${app_version}'
                    sh 'docker push hgwright/challenge_prompt_api:${app_version}'
                }
            }
            stage('Deploy Application'){
                steps{
                    sh "docker stack deploy --compose-file docker-compose.yaml challenge"
                }

            }
        }
    }