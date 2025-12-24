# Cloud-based log monitoring and alerting system deployed on AWS EC2
## ☁️ Cloud-Based Log Monitoring & Alerting System (AWS)

### 📌 Project Overview
This project implements a cloud-based log monitoring and alerting system deployed on an AWS EC2 Linux instance. It continuously generates and monitors application logs in real time and triggers alerts whenever new error events are detected, helping improve system observability and reliability.

### 🎯 Key Features
-Real-time log generation and monitoring 

-Automatic alerting on new ERROR log entries

-Avoids duplicate alerts using file position tracking

-Runs continuously as a background process on AWS EC2

-Lightweight and cost-effective cloud deployment

### 🧰 Technologies Used
-AWS EC2 (Amazon Linux 2)

-Python 3

-Linux

-Git & GitHub

### 🏗️ Architecture
-A Python script continuously generates application logs.

-Another Python script monitors the log file in real time.

-When a new ERROR entry appears, an alert is triggered.

-Both scripts run in the background on an AWS EC2 instance using nohup.
