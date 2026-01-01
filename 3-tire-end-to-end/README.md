# 3-Tier DevOps Application Deployment 🚀

[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
[![AWS](https://img.shields.io/badge/AWS-EKS-orange)](https://aws.amazon.com/eks/)
[![Docker](https://img.shields.io/badge/Docker-Container-blue)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Cluster-blueviolet)](https://kubernetes.io/)

---

## Overview
This project demonstrates a **full 3-tier web application deployment** using:

- **Frontend**: React/Angular/Vue (served via Nginx)
- **Backend**: Python Flask API
- **Database**: MySQL

The application is deployed on **AWS EKS** with **Ingress** for routing and **ELB** for public access.  
It is **containerized using Docker** and supports **CI/CD pipelines** via Jenkins.

---

## Architecture

Browser
   |
   v
Ingress Controller (Nginx)
   |---------------------------|
   |                           |
Frontend Service (NodePort)   Backend Service (ClusterIP)
   |                           |
   |                           |
Dockerized Frontend           Flask API
                              |
                              v
                        MySQL Database







**Key Components:**
- AWS EKS cluster (Kubernetes)
- AWS ELB for public access
- Frontend container served by Nginx
- Backend container (Flask API) connected to MySQL
- MySQL container for persistent storage
- Ingress routing for `/` (frontend) and `/api/*` (backend)

---

## Features
- Fully containerized 3-tier application
- REST API endpoints under `/api/*`
- Frontend served as SPA
- Backend connected to MySQL
- Ingress routing via Nginx
- CI/CD ready (Jenkins pipeline)
- Rolling updates without downtime

---

## Prerequisites
- Docker installed  
- kubectl configured  
- AWS CLI configured with proper IAM permissions  
- Terraform installed (if using IaC)

---

## Deployment Steps

### 1️⃣ Build Docker Images
```bash
# Frontend
docker build -t frontend-app ./frontend

# Backend
docker build -t backend-app ./backend


## Push Images to AWS ECR

aws ecr create-repository --repository-name frontend-app
aws ecr create-repository --repository-name backend-app

# Tag and push images
docker tag frontend-app:latest <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/frontend-app:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/frontend-app:latest

docker tag backend-app:latest <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/backend-app:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/backend-app:latest


    
#### Deploy on Kubernetes

kubectl apply -f k8s/mysql-deployment.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml

kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-service.yaml
kubectl apply -f k8s/ingress.yaml


## Access the apllication

Frontend URL: http://<ELB-DNS>/

Backend API URL:

http://<ELB-DNS>/api/hello

http://<ELB-DNS>/api/users


###CI/CD Integration

Jenkins can automate:

Docker image build

Push to ECR

Kubernetes deployment updates via kubectl apply

Supports rolling updates without downtime


####cleanup 


terraform destroy
aws ecr delete-repository --repository-name frontend-app --force
aws ecr delete-repository --repository-name backend-app --force



######Technologies Used

AWS: EKS, ELB, ECR

Kubernetes: Deployment, Service, Ingress

Docker: Containerization

Flask: Backend API

MySQL: Database

Nginx: Frontend server



#### Notes

Ensure MySQL tables exist before querying backend APIs.

Ingress routing: / → frontend, /api/* → backend.

IAM permissions required for EKS, ELB, and ECR operations.