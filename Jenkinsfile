pipeline {
    agent any
    stages {
	stage('installDependencies') {
	    steps {
		script {
		    load './env.groovy'
		}
		sshagent(credentials:["${env.sshcredentials}"]) {
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'sudo apt-get update'"
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'sudo apt-get install -y docker.io'"
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'sudo apt-get install -y docker-compose'"
	    }
	}
    }
	stage("makeDirs") {
	    steps {
		sshagent(credentials:["${env.sshcredentials}"]) {
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'mkdir API'"
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'mkdir setup'"
		}
	    }
	}
        stage('moveFiles') {
	    steps {
		    sh "chmod 400 ${env.pkey}"
		    moveFiles('docker-compose.yml', '/home/ubuntu')
	 	    moveFiles('API/api.py', '/home/ubuntu/API')
		    moveFiles('API/Dockerfile', '/home/ubuntu/API')
		    moveFiles('API/requirements.txt', '/home/ubuntu/API')
		    moveFiles('setup/setup.py', '/home/ubuntu/setup')
		    moveFiles('setup/create_database.sql', '/home/ubuntu/setup')
		    moveFiles('setup/create_table.sql', '/home/ubuntu/setup')
		    moveFiles('setup/insert_data.sql', '/home/ubuntu/setup')
		    moveFiles('setup/Dockerfile', '/home/ubuntu/setup')
		    sh 'echo Files Moved Successfully!'
	    }
	}
	stage('startAPI') {
	    steps {
		sshagent(credentials:["${env.sshcredentials}"]) {
                    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'docker-compose up --build'"
	    }
	}
    }
}


void moveFiles(file, path) {
    load './env.groovy'
    if ("${env.EC2_PUBLIC_IP}" == "") {
	    throw new Exception('Missing value for EC2 Public IP')
	}
    if ("${env.sshcredentials}" == "") {
	    throw new Exception("Missing value for sshcredentials")
	}
    if ("{env.pkey}" == "") {
	    throw new Exception("Missing value for pkey")
	}
    sshagent(credentials:["${env.sshcredentials}"]) {
	sh "scp -i ${env.pkey} -o StrictHostKeyChecking=no ${file} ubuntu@${env.EC2_PUBLIC_IP}:${path}"
    }
}