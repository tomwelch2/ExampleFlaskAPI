<h1>Example Flask REST API</h1>

<h2>Repository Structure</h2>

```
.
├── airflowkey.pem
├── API
│   ├── api.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── env.groovy
├── Jenkinsfile
├── setup
│   ├── create_database.sql
│   ├── create_table.sql
│   ├── Dockerfile
│   ├── insert_data.sql
│   └── setup.py
└── terraform
    ├── main.tf
    ├── outputs.tf
    ├── terraform.tfstate
    ├── terraform.tfstate.backup
    └── terraform.tfvars

```

The repository contains three main folders (API, setup and terraform) which are
responsible for creating the REST API, populating a MySQL docker instance and creating
AWS cloud infrastructure to run the API on respectively. the API and setup folders
are designed to be ran in Docker and are used in the **docker-compose.yml** file 
to build the API. The terraform folder, along with the Jenkinsfile, is only to be
used if the user wished to host the API on a AWS EC2 instance - if the user wished to
run the API locally, a simple ```docker-compose up --build``` command can be used which
will allow local access to the API via the endpoint **http://0.0.0.0:5000**.

<h1>Architecture</h1>

Flask and Flask Restful Python libraries have been used to create a simple REST API
which returns fake "employee" data with features such as salary, branch_id and firstname.
The data used for the API is obtained through a MySQL database which is created and populated
once the ```docker-compose up --build``` command is issued and is connected directly to the API
using Pandas and SQLAlchemy. There is only currently one endpoint, **/all** in the API which
returns all data on all employees (roughly 5 rows just for demonstrative purposes).

In terms of cloud infrastructure, Terraform was used to automatically provision an EC2 instance
to run the API on, with a CI/CD pipeline ran via Jenkins being used to install dependencies and
move the API files to the EC2 instance so that it can be accessed outside of localhost.


<h1>Running the code</h1>
<h2>Local Mode </h2>

To run the API locally, simply run a ```docker-compose up``` command in the base directory of the 
repository and wait for the setup to finish. Once the setup is complete, the API will be available
at **http://0.0.0.0:5000/all**.

<h2>In the cloud</h2>

To run the API on a AWS EC2 instance (allowing for connections from outside localhost) change
to the **terraform** directory and open the ```terraform.tfvars``` file. Edit the file
to reflect the individual keys for your AWS account (Access Key, Secret Key, Region) and
the key-file to be used to allow access into the EC2 instance via SSH. 

Once these configurations have been applied, run ```terraform apply``` in the **terraform**
directory and enter **yes** when asked to do so. The terminal will output an IP address, note
this IP address down as you will need it later.

https://github.com/tomwelch2/ExampleFlaskAPI/blob/master/images/Screenshot%20from%202021-04-21%2015-28-01.png




