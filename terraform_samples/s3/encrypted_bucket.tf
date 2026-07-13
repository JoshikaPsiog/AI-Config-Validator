resource "aws_s3_bucket" "encrypted_bucket" {
  bucket = "demo-bucket"

  tags = {
    Name = "Demo"
  }
}