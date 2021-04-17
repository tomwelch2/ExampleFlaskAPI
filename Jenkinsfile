pipeline {
    agent any
    stages {
	stage('installDependencies') {
	    script {
		load './env.groovy'
	    }
	    steps {
		sshagent(credentials:["${env.sshcredentials}"]) {
		    sh 'sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release'
		    sh 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg'
		    sh 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null'
		    sh 'sudo apt-get update'
		    sh 'sudo apt-get install -y docker-ce docker-ce-cli containerd.io'
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
	stage('testAPI') {
	    steps {
		sshagent(credentials:["${env.sshcredentials}"]) {
	            sh 'python3 tests/test.py'
		}
	    }
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
