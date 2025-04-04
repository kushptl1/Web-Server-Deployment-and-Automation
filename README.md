# 🏗️ AWS Web Server Deployment using Terraform (Modular)

This project automates the deployment of a secure and scalable web server infrastructure on AWS using **modular Terraform**.

## 🚀 Project Overview

This setup includes:

- A custom **VPC** with public and private subnets
- An **EC2 instance** running Apache in a private subnet
- An **Application Load Balancer (ALB)** in the public subnets
- An **S3 bucket** for storing static website files
- A **DynamoDB table** for storing user login details

All resources are created using **Terraform modules** for better structure and reusability.

---

## 📁 Project Structure

Py files #DynamoDB Table Creation and Interaction using Python Boto3

```bash
part2 # Web Server Deployment on EC2
├── main.tf   
Web Server Deployment on EC2

part2_task2  #Automating Deployment with Terraform 
├── main.tf                  # Top-level orchestrator
├── modules/
│   ├── vpc/
│   ├── ec2/
│   ├── alb/
│   ├── s3/
│   └── dynamodb/


