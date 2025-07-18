resource "aws_instance" "webapp" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = "bastion"
  vpc_security_group_ids = ["sg-0b09597d8d8189c49"]
  user_data              = file("userdata.sh")

  tags = {
    "Name" = "${var.project_name}-${var.project_env}-webserver"
  }
}