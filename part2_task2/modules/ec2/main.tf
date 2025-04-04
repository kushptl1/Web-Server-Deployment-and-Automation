
variable "vpc_id" {}
variable "private_subnet_id" {}
variable "ec2_sg_id" {}

resource "aws_instance" "web" {
  ami           = "ami-00a929b66ed6e0de6"
  instance_type = "t2.micro"
  subnet_id     = var.private_subnet_id
  vpc_security_group_ids = [var.ec2_sg_id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl enable httpd
              systemctl start httpd
              echo "<h1>Hello from EC2 in Private Subnet</h1>" > /var/www/html/index.html
              EOF
}

output "instance_id" {
  value = aws_instance.web.id
}
