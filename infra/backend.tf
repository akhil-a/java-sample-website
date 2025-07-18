terraform {
  backend "s3" {
    bucket = "java-sample-app-akhil"
    key    = "${var.project_name}/${var.project_env}/terraform.tfstate"
    region = "ap-south-1"
  }
}
