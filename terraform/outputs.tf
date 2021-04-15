output "aws_ec2_public_ip" {
	value = aws_instance.APIInstance.public_ip
}
