# AWS DevOps Architecture Diagram

                    Developer
                        │
                        │
                  Git Push Code
                        │
                        ▼
                GitHub Repository
                        │
                        │
             GitHub Actions CI Pipeline
                        │
                        ▼
                 Python Syntax Check
                        │
                        ▼
                AWS EC2 Instance
               (Ubuntu + Flask App)
                        │
         ┌──────────────┼──────────────┐
         │              │              │
         ▼              ▼              ▼
    Web Browser      CloudWatch       Amazon S3
  HTTP Port 5000     Monitoring       File Storage