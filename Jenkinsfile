pipeline {
    agent any
    stages {
	stage('installDependencies') { 
	    steps {
		script {
		    load './env.groovy' //Loading environment variables
		}
		sshagent(credentials:["${env.sshcredentials}"]) {
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'sudo apt-get update'"
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'sudo apt-get install -y docker.io'"
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'sudo apt-get install -y docker-compose'"
	    }
	}
    }
	stage("makeDirs") { //Makes directories expected by docker-compose file
	    steps {
		sshagent(credentials:["${env.sshcredentials}"]) {
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'mkdir API'"
		    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'mkdir setup'"
		}
	    }
	}
        stage('moveFiles') { //Moves all files via SCP to server 
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
		    moveFiles('setup/create_users_tbl.sql', '/home/ubuntu/setup')
		    moveFiles('setup/add_admin_user.sql', '/home/ubuntu/setup')
		    moveFiles('./nginx.conf', '/home/ubuntu')
		    sh 'echo Files Moved Successfully!'
	    }
	}
	stage('startAPI') { //Builds and runs Docker images with docker-compose
	    steps {
		sshagent(credentials:["${env.sshcredentials}"]) {
                    sh "ssh -t -t ubuntu@${env.EC2_PUBLIC_IP} -o StrictHostKeyChecking=no 'sudo docker-compose up --build'"
	    }
	}
	}
}

}

void moveFiles(file, path) { //Function takes a file to move and a path on the server to move file to
    load './env.groovy'
    if ("${env.EC2_PUBLIC_IP}" == "") { //Checking if credentials within env file have been supplied
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
