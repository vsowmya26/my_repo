provider "aws" {
    region = ap-south-1
  }
resource "ec2" "name" {
    ami = "ami-03f4878755434977f"
    instance_type = "t2.micro"
    tags {
        Name = "NewInstancethrough_Terraform"
    }
}