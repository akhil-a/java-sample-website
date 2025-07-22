terraform {
  backend "s3" {
    bucket = "terraform-statefiles-akhil10anil"
    key    = "java-sample-app/terraform.tfstate"
    region = "ap-south-1"
  }
}
