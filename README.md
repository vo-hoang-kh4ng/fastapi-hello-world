# FastAPI Hello World

This repository contains a basic "Hello World" application built with FastAPI. This guide provides step-by-step instructions for running the project locally, using Docker, and deploying it to Kubernetes with Minikube.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Running Locally](#running-locally)
- [Running with Docker](#running-with-docker)
- [Deploying to Kubernetes with Minikube](#deploying-to-kubernetes-with-minikube)

---

## Prerequisites

Ensure the following are installed on your system:

1. [Python 3.8+](https://www.python.org/downloads/)
2. [Docker](https://www.docker.com/)
3. [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
4. [Minikube](https://minikube.sigs.k8s.io/docs/start/)
5. [Git](https://git-scm.com/)

---

## Running Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/vo-hoang-kh4ng/fastapi-hello-world.git
   cd fastapi-hello-world
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Start the FastAPI application:
   ```bash
   pip install -r requirements.txt
5.Open your browser and navigate to:
 ```bash
App: http://127.0.0.1:8000

