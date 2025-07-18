terraform {
  backend "s3" {
    bucket = "java-sample-app-akhil"
    key    = "terraform.tfstate"
    region = "ap-south-1"
  }
}
