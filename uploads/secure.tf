resource "aws_s3_bucket" "demo" {
  bucket = "my-demo-bucket"
}

server_side_encryption_configuration {
}