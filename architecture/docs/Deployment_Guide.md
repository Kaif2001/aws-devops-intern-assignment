# Deployment Guide

# AWS DevOps Internship Assignment

## Overview

This guide explains how to deploy the Flask application on an AWS EC2 instance and configure the required AWS services.

---

# Prerequisites

- AWS Account
- Ubuntu EC2 Instance
- Git
- Python 3
- pip
- GitHub Account
- Terraform
- AWS CLI

---

# Step 1 - Launch EC2 Instance

- Login to AWS Console.
- Open EC2 Dashboard.
- Launch Ubuntu t3.micro instance.
- Configure Security Group.

Allowed ports:

- 22 (SSH)
- 5000 (Flask Application)
- 80 (HTTP)

Connect to the instance using SSH.

---

# Step 2 - Clone Repository

```bash
git clone https://github.com/Kaif2001/aws-devops-intern-assignment.git
```

```
cd aws-devops-intern-assignment/app
```

---

# Step 3 - Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install -r requirements.txt
```

---

# Step 4 - Run Flask Application

```bash
python3 app.py
```

The application becomes available at

```
http://<EC2-Public-IP>:5000
```

---

# Step 5 - Configure Amazon S3

- Create an S3 bucket.
- Upload project files if required.
- Verify uploaded objects.

---

# Step 6 - Configure CloudWatch

Monitor

- CPU Utilization
- Network In
- Network Out

CloudWatch automatically collects EC2 metrics.

---

# Step 7 - Terraform

Terraform files are available inside

```
terraform/
```

Commands

```bash
terraform init
terraform plan
terraform apply
```

---

# Step 8 - GitHub Actions

Every push to the GitHub repository automatically performs

- Checkout Repository
- Setup Python
- Install Dependencies
- Python Syntax Check

---

# Step 9 - Load Testing

Load testing is performed using Grafana k6.

Command

```bash
k6 run load-testing/load-test.js
```

---

# Deployment Completed

The application is successfully deployed on AWS EC2.

Integrated AWS services

- Amazon EC2
- Amazon S3
- Amazon CloudWatch
- Terraform
- GitHub Actions