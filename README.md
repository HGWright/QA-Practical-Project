# QA-Practical-Project

### Introduction

The brief for this project can be quoted directly from the project specification:

* "You are required to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together."

* "The final deliverable for this project is a completed CI Pipeline with full documentation around the utilisation of supporting tools."

These two statments are im my opinion the keys to being successful in this project.

It was layed out that the application needed to be a 4 service application with 3 api's and a web server.

![image](https://user-images.githubusercontent.com/84939917/126123289-8d3db024-5420-4d63-9279-2ac2ac06b779.png)

For my application I decided to make a party game challenge generator, whereby the user recieves a challenge and if the server precieves the challenge to be too easy, then an additional challenge is added.

In order to complete the MVP we were given a list of tools we must use:

* Kanban Board: Asana or an equivalent Kanban Board (Trello Board)
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL

![image](https://user-images.githubusercontent.com/84939917/126133447-2818fd5b-35e2-480b-836c-0699cf7c69ef.png)

We are using:

* Trello for Project Tracking
* VSCode for Programming
* Git for Version Control
* Jenkins for CI server
* Pytest automated with Jankins for Testing
* Docker Compose for Build and Push
* Ansible for Configuration
* Docker Swarm deployed my Jenkins to Deploy
* NGINX for Load Balancing, using a reverse proxy
* GCP SQL server for the Database Layer

### Trello Board

Here is my trello board, using user stories and the AGILE framework I have created and completed a Sprint Backlog to meet all of the requirements of the MVP for this project.

![image](https://user-images.githubusercontent.com/84939917/126123868-f1728a63-3b78-4d27-b0e6-87c57d606d89.png)

### Risk Assessment

Below is my initial risk assessment for this project.

![image](https://user-images.githubusercontent.com/84939917/126137169-37ce7d93-0bdd-4487-b2d1-3a97b7f4b7cc.png)

After I implenented the control measures for each risk, I have reassessed the chance to happen and the severity of each of the risks which can be seen below.

![image](https://user-images.githubusercontent.com/84939917/126137442-2567fc01-4616-458a-9d7d-45c7681cbe7f.png)


### Entity Relationship Diagram (ERD)

There is only one table in a single database for this project. It is used to store the information of the previous challenges, and is then queried to return the 5 most recent challenges to the frontend server.

![image](https://user-images.githubusercontent.com/84939917/126124391-782ac047-9101-4631-a655-e794827b70d4.png)



### Interacting with the Application

Using Docker Swarm we are able to configure a group of VM's to perform a task. This means that you are lss likely to overload a single VM and as a result the application can deal with more requests simultaniously. In addition to this we use replicas (making more than 1 copy of all of our services across the swarm) to allow multiple requests to be dealt with simultaniously.

The diagram below shows the configuration of my virtual machines, and how a user would interact with them. In this case we are using NGINX as a load balancer in order to distribute requests equally over both the manager and worker vm's in the swarm, this just further reduces the load on any set of replicas and any individual vm.

![image](https://user-images.githubusercontent.com/84939917/126126620-471bc0b1-2bbc-4ff6-a693-36de5ba79df7.png)

### My Services

![image](https://user-images.githubusercontent.com/84939917/126127589-ebbb7ca9-7add-4dfe-8d9b-5771f7e20768.png)

I have shown my 4 services in the image above:
* The 'Word_API' generates a random word from a list of words when requested by the server.
* The 'Number_API' generates a random number from a range of numbers when requested by the server.
* The 'Prompt_API' recieves the word and the number from the previous api's, and depending on the word and the number returns either a random prompt from a list or just returns a string.

### Ansible

Ansible is a configuration management tool. I am using it to configure my VM's. The best thing about ansible is that it is declerative, meaning that it can be ran as many times as you like over the same VM and if it sees that that task is not needed because the module it was going to install is already there ansible will just skip over that task and move onto the next one. A useful example of this would be adding a new VM to the swarm, instead of having to run ansible just for that new VM, you can add that VM to the inventory.yaml and the and then just run ansible. All of the old machines will remain unchanged and the new one will be configured exactly the same way as them.

### Testing

Testing for the server
![image](https://user-images.githubusercontent.com/84939917/126129498-cc4b320a-ca95-4169-82d8-adc861f4240c.png)

Testing for word_api
![image](https://user-images.githubusercontent.com/84939917/126129585-6da90e81-aefe-4c6b-94a4-34420b79ac47.png)

Testing for number_api
![image](https://user-images.githubusercontent.com/84939917/126129672-9a35f695-1c3a-4a5c-9c1c-254620e00224.png)

Testing for prompt api
![image](https://user-images.githubusercontent.com/84939917/126129768-74a224cb-5dde-4324-9524-d242968c666c.png)

Testing is a very omportant part of developing an application. Testing ensures that your application behaves as you would expect it too under a number of different situations.

I have done unit tests for this application as they are the tests that are required, they test almost all of every service of my application and I am happy with the coverage I have achieved. I was unable to get reports of my coverage so these screenshots from the terminal VSCode will have to do

### Jenkins

Jenkins is perhaps the most important tool we have used in this application, the ability to build, test and deploy the application automatically after every git commit to the main branch is what is going to allow us to perform a rolling update.

A rolling update is when an update to the service does not require the service to be taken down. This means that users experience with the website would not be affected by any updates that we make. In order to achieve a rolling update we can use replicas of our services so we can keep using the application while it is being updated.

We use a Jenkinsfile in our application too list the tasks we wish for Jenkins to perform and then when Jenkins pulls our repository from GitHub via a webhook it will find the Jenkins file and perform the actions within.

My Jenkinsfile has 4 stages:

* Build the Application
* Test the Application
* Push the Containers
* Deply the Application

# Building the Application
This is the easiest step, all we have to do is make single version of each service.

![image](https://user-images.githubusercontent.com/84939917/126134417-4e5d2b06-595b-46bd-bf9c-74b1f7158839.png)


# Testing the Application

![image](https://user-images.githubusercontent.com/84939917/126132999-7229cf97-df91-44a2-bec1-842902d819b6.png)

To test the application we have to install the requirements that arnt installed with Ansible, then test our application with pytest just like we would do in the VSCode terminal.

# Pushing the Containers

![image](https://user-images.githubusercontent.com/84939917/126134503-4d731f46-a7d0-4941-9ed0-139502b64007.png)

This process is pushing the containers up to docker hub, so we have to login with a jenkins credential (along with the other credential for the DATABASE_URI). The containers are pushed so that they can be deployed in the next stage using docker swarm and the docker compose file.

# Deploying the Application

![image](https://user-images.githubusercontent.com/84939917/126134604-697e7c30-bcaa-4dbe-b9d1-c9bc6faddbcf.png)

To deploy the application we simply fire up the swarm using the containers on dockerhub that we pushed in the previous step.

### Frontend

Below you can see the front end of my application, it is designed to be the most barebones application possible and just perform the simple required functions. This was accessed through the NGINX load balancing VM.

![image](https://user-images.githubusercontent.com/84939917/126135394-e26b7258-f539-42f9-af7f-1dca7287dd48.png)

### Future Improvments

* I would like to get coverage reports from Jenkins
* I could setup users and login functionality
* I could drastically imporve the frontend of the web server


### Authors

Henry Wright
