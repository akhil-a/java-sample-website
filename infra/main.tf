resource "aws_instance" "webapp" {
  count                  = 2
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = "bastion"
  vpc_security_group_ids = ["sg-0b09597d8d8189c49"]
  user_data              = file("userdata.sh")

  tags = {
    "Name" = "${var.project_name}-${var.project_env}-webserver-${count.index + 1}"
  }
}

resource "aws_route53_record" "route53_record" {
  zone_id = data.aws_route53_zone.my_domain.zone_id
  name    = "${var.project_name}.${var.project_env}.${var.domain_name}"
  type    = "A"
  ttl     = 300
  records = aws_instance.webapp[*].public_ip

}

output "java_app_url" {
  value = "http://${aws_route53_record.route53_record.name}:8080"

}
