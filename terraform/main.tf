resource "aws_instance" "devops_server" {

  ami           = "ami-006f82a1d5a27da54"

  instance_type = var.instance_type

  tags = {
    Name = var.instance_name
  }

}