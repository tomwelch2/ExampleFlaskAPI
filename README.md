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
returns all data on all employees (roughly 10 rows just for demonstrative purposes).

In terms of cloud infrastructure, Terraform was used to automatically provision an EC2 instance
to run the API on, with a CI/CD pipeline ran via Jenkins being used to install dependencies and
move the API files to the EC2 instance so that it can be accessed outside of localhost.









