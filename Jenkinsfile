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
	    }
	}
    }
        stage('moveFiles') {
	    steps {
		    sh "chmod 400 ${env.pkey}"
		    moveFiles('docker-compose.yml')
	 	    moveFiles('API/api.py')
		    moveFiles('setup/setup.py')
		    moveFiles('setup/create_database.sql')
		    moveFiles('setup/create_table.sql')
		    moveFiles('setup/insert_data.sql')
		    sh 'echo Files Moved Successfully!'
	    }
	}
    }
	post {
	    success {
		sh "echo Success!"
	    }
	    failure {
		sh "Failed :("
	    }
	}
}


void moveFiles(file) {
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
	sh "scp -i ${env.pkey} -o StrictHostKeyChecking=no ${file} ubuntu@${env.EC2_PUBLIC_IP}:/home/ubuntu"
    }
}
