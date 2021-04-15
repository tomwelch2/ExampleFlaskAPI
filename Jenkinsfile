pipeline {
    agent any
    stages {
        stage('moveFiles') {
	    steps {
		sh "chmod 400 airflowkey.pem"
		moveFiles('docker-compose.yml')
		moveFiles('API/api.py')
		moveFiles('setup/setup.py')
		moveFiles('setup/create_database.sql')
		moveFiles('setup/create_table.sql')
		moveFiles('setup/insert_data.sql')
		moveFiles('tests/test.py')
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
	sh "scp -i airflowkey.pem -o StrictHostKeyChecking=no ${file} ubuntu@${env.EC2_PUBLIC_IP}:/home/ubuntu"
    }
}
