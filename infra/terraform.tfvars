project_name   = "java-webapp"
project_env    = "dev"
instance_type  = "t2.micro"
ami_id         = "ami-0a1235697f4afa8a4"
vcp_cidr_block = "172.16.0.0/16"
enable_nat_gw  = true
server_ports   = [80, 443]
sec_groups     = ["sg-0b09597d8d8189c49"]
