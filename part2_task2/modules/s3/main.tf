
variable "bucket_name" {}

resource "aws_s3_bucket" "static_site" {
  bucket        = var.bucket_name
  force_destroy = true
}
