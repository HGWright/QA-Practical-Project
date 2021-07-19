pipeline{
        agent any
        environment {
            DATABASE_URI = credentials('DATABASE_URI')
            docker_password = credentials('docker_passoword')
            app_version = 'v1'
        }
        stages{
            stage('Build Container'){
                steps{
                    sh "sudo docker-compose up -d --build"
                }
            }
            stage('Testing the Application'){
                steps{
                    sh "sudo pip3 install -r requirements.txt"
                    sh "pytest ./number_api --cov=app --cov-report html"
                    sh "pytest ./word_api --cov=app --cov-report html"
                    sh "pytest ./prompt_api --cov=app --cov-report html"
                    sh "pytest ./server --cov=app --cov-report html"
                    archiveArtifacts artifacts: 'number_api/htmlcov/', 'word_api/htmlcov/', 'server/htmlcov/', 'prompt_api/htmlcov/'
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