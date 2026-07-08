# AWS DevOps Internship Assignment

## Project Overview

This project demonstrates a production-style deployment of a Flask application on AWS using DevOps best practices.

## Technologies Used

- AWS EC2
- AWS S3
- AWS CloudWatch
- Terraform
- GitHub Actions
- Python Flask
- Git

---

## Project Structure

```
AWS-DevOps-Intern-Assignment/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── main.tf
│   └── outputs.tf
│
├── screenshots/
│   ├── cloudwatch/
│   └── s3/
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
└── README.md
```

---

## Features

- Flask Application
- Health Endpoint
- Ready Endpoint
- Info Endpoint
- EC2 Deployment
- S3 Storage
- CloudWatch Monitoring
- Terraform Infrastructure
- GitHub Actions CI

---

## Endpoints

### Home

```
/
```

### Health

```
/health
```

Returns

```json
{
    "status":"healthy",
    "application":"AWS DevOps Internship Assignment",
    "developer":"Mohammed Kaif"
}
```

### Ready

```
/ready
```

Returns

```json
{
    "status":"ready"
}
```

### Info

```
/info
```

Returns

```json
{
    "application":"AWS DevOps Internship Assignment",
    "developer":"Mohammed Kaif",
    "cloud":"AWS",
    "deployment":"EC2",
    "monitoring":"CloudWatch",
    "ci_cd":"GitHub Actions"
}
```

---

## AWS Services Used

### EC2

Application Hosting

### S3

Object Storage

### CloudWatch

Application Monitoring

---

## Terraform

Terraform configuration files are available in the terraform folder.

Files:

- provider.tf
- variables.tf
- main.tf
- outputs.tf

---

## GitHub Actions

GitHub Actions automatically

- Checkout Repository
- Install Python
- Install Dependencies
- Check Python Syntax

---

## Developer

Mohammed Kaif