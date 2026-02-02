🚀 CI/CD Pipeline with Docker, Kubernetes & Ansible (Production-Style)
📌 Overview

This project demonstrates a production-style CI/CD workflow for a backend API using:

GitHub Actions for CI

Docker for containerization

Kubernetes for orchestration

Ansible for deployment and rollback automation

The goal of this project is not to show a simple app, but to showcase how modern DevOps systems are designed, deployed, and operated.

🎯 Key Objectives

Build immutable Docker images tagged with Git commit SHAs

Inject build-time metadata into containers

Deploy applications to Kubernetes using rolling updates

Automate deployments and rollbacks using Ansible

Avoid manual YAML edits during deployments (production best practice)

🧠 Architecture & Flow

Developer Commit
      ↓
GitHub Actions (CI)
      ↓
Docker Image (tagged with commit SHA)
      ↓
Local Image Registry (minikube Docker)
      ↓
Ansible Deployment
      ↓
Kubernetes Deployment (Rolling Update)
      ↓
Service → Pods

🧩 Tech Stack

| Layer                 | Technology     |
| --------------------- | -------------- |
| Language              | Python (Flask) |
| CI                    | GitHub Actions |
| Containerization      | Docker         |
| Orchestration         | Kubernetes     |
| Deployment Automation | Ansible        |
| Local Cluster         | Minikube       |


📁 Project Structure
ci-cd_demo/
├── app/
│   └── app.py
├── docker/
│   └── Dockerfile
├── k8s/
│   └── base/
│       ├── deployment.yaml
│       └── service.yaml
├── ansible/
│   ├── inventory
│   ├── deploy.yml
│   └── rollback.yml
└── .github/
    └── workflows/
        └── pipeline.yml


🐳 Docker (Production-Grade)
Key Docker Practices Used

Non-root container user

Slim base image

Build-time arguments (ARG)

Runtime environment variables (ENV)

Git commit metadata baked into image

Image Tagging Strategy

backend-api:<git-commit-sha>

This ensures:

Traceability

Safe rollbacks

Immutable artifacts



☸️ Kubernetes Design
Why Deployment (not Pod)?

Self-healing

Rolling updates

Scaling

Production readiness

Features Used

RollingUpdate strategy

Readiness & liveness probes

Multi-replica deployment

ClusterIP service for stable networking

Deployment YAML (Key Concept)

The image tag is not hardcoded:
image: backend-api:PLACEHOLDER
Image versions are injected dynamically by Ansible, not Git.

⚙️ CI Pipeline (GitHub Actions)

The CI pipeline:

1.Checks out code

2.Builds Docker image

3.Tags image using github.sha

4.Injects commit metadata using build arguments

Why Commit SHA?

Every deployment maps to exact code

No ambiguity during debugging

Industry standard practice


🤖 Ansible (Deployment & Rollback)
Why Ansible?

Separates deployment logic from Kubernetes manifests

Eliminates manual YAML edits

Enables safe, repeatable rollouts

Deploy Command

ansible-playbook -i ansible/inventory ansible/deploy.yml \
  -e image_tag=<commit-sha>

Rollback Command

ansible-playbook -i ansible/inventory ansible/rollback.yml \
  -e image_tag=<previous-sha>


🧪 Deployment Verification
kubectl get pods
kubectl logs -l app=backend-api
kubectl port-forward svc/backend-api 8080:80
curl http://localhost:8080/status

🏆 What This Project Demonstrates

Real CI/CD thinking (not scripts)

Docker best practices

Kubernetes deployment patterns

Ansible as an operations tool

Production-style rollout & rollback

Debugging real DevOps issues (ErrImagePull, CrashLoop, rollout failures)


