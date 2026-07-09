# Security Summary

## AWS DevOps Internship Assignment

### Overview

This project follows basic AWS security best practices to protect the application and cloud infrastructure.

---

## 1. IAM Security

- IAM user was used instead of the AWS root account.
- Least privilege principle was followed.
- AWS Access Keys are used only for Terraform.
- Root account is not used for daily operations.

---

## 2. EC2 Security Group

The EC2 instance allows only the required ports.

| Port | Purpose |
|------|---------|
|22|SSH Access|
|5000|Flask Application|
|80|HTTP (Optional)|

All other ports remain closed.

---

## 3. Application Security

The Flask application exposes only required endpoints.

Available endpoints

- /
- /health
- /ready
- /info

No passwords or AWS credentials are stored in the application source code.

---

## 4. GitHub Security

The project source code is stored in GitHub.

GitHub Actions automatically validates every code push.

Sensitive files are excluded using the .gitignore file.

Ignored files include

- terraform.tfstate
- .terraform/
- __pycache__/
- venv/

---

## 5. Terraform Security

Terraform configuration files are stored separately.

Terraform state files are excluded from GitHub.

Provider binaries are also excluded from version control.

---

## 6. Monitoring

Amazon CloudWatch is configured for

- CPU Utilization
- Network In
- Network Out

Monitoring helps identify application issues and resource usage.

---

## 7. Amazon S3

Amazon S3 is used for storing project data and backups.

Public access remains blocked unless specifically required.

---

# Conclusion

This project demonstrates secure deployment practices using AWS IAM, EC2 Security Groups, Amazon S3, Terraform, GitHub Actions and Amazon CloudWatch while following basic cloud security best practices.