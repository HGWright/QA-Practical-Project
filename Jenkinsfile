pipeline{
        agent any
        environment {

            app_version = 'v1'
            rollback = 'false'
        }
        stage{
            stage('Build Image'){
                steps{
                    
                            docker.withRegistry("${DOCKER_REGISTRY}", 'docker-registry-credentials') {
                            def img = docker.build("${CONTAINER}:${VERSION}")
                            img.push()
                            sh "docker rmi ${img.id}"
                    
                }
            }
            }
        }
            stage('Tag & Push Image'){
                steps{
                    
                        if (env.rollback == 'false'){
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                                image.push("${env.app_version}")
                            
                        }
                    }
                }
            }
            stage('Test Application'){
                steps{
                    sh python3 -m venv venv
                    . ./venv/bin/activate
                    sh pip3 install -r requirements.txt
                    sh cd /home/henry/QA-Practical-Project-4/number_api && sh pytest
                    sh cd /home/henry/QA-Practical-Project-4/word_api && sh pytest
                    sh cd /home/henry/QA-Practical-Project-4/prompt_api && sh pytest
                    sh cd /home/henry/QA-Practical-Project-4/server && sh pytest
                    sh sudo rm -rf venv
                }
            }
            stage('Deploy App'){
                steps{
                    withCredentials([
                        usernamePassword(
                            credentialsId: 'docker-registry-credentials',
                            usernameVariable: 'DOCKER_USER',
                            passwordVariable: 'DOCKER_PASSWORD'
                            sh "docker stack deploy --compose-file docker-compose.yaml challenge"
                }
            }
        }