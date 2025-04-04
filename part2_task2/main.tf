provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "./modules/vpc"
}

module "ec2" {
  source            = "./modules/ec2"
  vpc_id            = module.vpc.vpc_id
  private_subnet_id = module.vpc.private_subnet_id
  ec2_sg_id         = module.vpc.ec2_sg_id
}

module "alb" {
  source            = "./modules/alb"
  vpc_id            = module.vpc.vpc_id
  public_subnet_ids = module.vpc.public_subnet_ids
  ec2_instance_id   = module.ec2.instance_id
  alb_sg_id         = module.vpc.alb_sg_id
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = "my-static-web-bucket-kush"
}

module "dynamodb" {
  source     = "./modules/dynamodb"
  table_name = "UserLogins"
}

