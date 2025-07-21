
variable "project_name" {
  description = "project name"
  type        = string
}

variable "project_env" {
  description = "project environment"
  type        = string
}

variable "instance_type" {
  description = "t2 micro usually"
  type        = string
}

variable "ami_id" {
  description = "ami id"
  type        = string
}

variable "sec_groups" {
  description = " security groups ID"
  type        = list(string)
}

variable "domain_name" {
  description = "domain_name in route53"
  type        = string
}