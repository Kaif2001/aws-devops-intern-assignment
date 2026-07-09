# Final Report

# AWS DevOps Internship Assignment

Developer: Mohammed Kaif

---

# Project Objective

The objective of this project was to deploy a production-style Flask web application on AWS using DevOps best practices while utilizing AWS Free Tier services.

The project demonstrates cloud deployment, Infrastructure as Code, monitoring, CI/CD automation, security practices and performance testing.

---

# Technologies Used

- Python Flask
- AWS EC2
- Amazon S3
- Amazon CloudWatch
- Terraform
- GitHub Actions
- Git
- Grafana k6

---

# Infrastructure

The infrastructure includes

- Ubuntu EC2 Instance
- Security Group
- Amazon S3 Bucket
- CloudWatch Monitoring
- Terraform Configuration

---

# Application Features

The Flask application provides

- Home Page
- Health Endpoint
- Ready Endpoint
- Info Endpoint

Available endpoints

/

/health

/ready

/info

---

# CI/CD

GitHub Actions automatically performs

- Repository Checkout
- Python Setup
- Dependency Installation
- Python Syntax Validation

---

# Monitoring

Amazon CloudWatch was configured to monitor

- CPU Utilization
- Network In
- Network Out

---

# Load Testing

Load testing was performed using Grafana k6.

Configuration

- Virtual Users: 20
- Duration: 30 Seconds

Results

- Total Requests: 361
- Success Rate: 99.72%
- Average Response Time: 65.74 ms
- Failed Requests: 1

The application remained stable during testing.

---

# Security

Security practices implemented

- IAM User instead of Root User
- Security Groups
- Least Privilege Principle
- Access Keys for Terraform
- CloudWatch Monitoring

---

# Challenges

Some challenges encountered during implementation

- Terraform initialization
- GitHub Personal Access Token permissions
- CloudWatch monitoring configuration
- Load testing setup using k6

Each issue was successfully resolved.

---

# Future Improvements

Possible improvements

- HTTPS using Nginx
- Custom Domain
- Auto Scaling
- Load Balancer
- RDS Database
- Docker
- Kubernetes

---

# Conclusion

The AWS DevOps Internship Assignment was successfully completed using AWS Free Tier services.

The project demonstrates cloud deployment, Infrastructure as Code, CI/CD automation, monitoring, security and performance testing using industry-standard DevOps tools.