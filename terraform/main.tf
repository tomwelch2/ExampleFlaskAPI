provider "aws" {
	access_key = var.keys.aws_access_key_id
	secret_key = var.keys.aws_secret_access_key
	region = var.aws_default_region
}


variable "keys" {
	type = map
	description = "A map consisting of AWS Access Key and AWS Secret Key"
}

variable "aws_default_region" {
	type = string
	description = "Region name tied to AWS account"
}


variable "pkey" {
	type = string
	description = "Key file for AWS EC2 Instance"
}

resource "aws_instance" "APIInstance" {
	ami = "ami-09c6eba41572dea7f"
	instance_type = "t2.micro"
	key_name = var.pkey
	
	tags = {
	    Name = "APIInstance"
	}
}
