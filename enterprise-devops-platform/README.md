# Enterprise DevOps Platform (GitHub CI/CD + EKS)

This repository demonstrates a **CI/CD pipeline** using **GitHub Actions** that:
1) builds a Docker image,
2) runs a container security scan (Trivy),
3) pushes the image to **Docker Hub**,
4) deploys to **Amazon EKS** using `kubectl`.

It also includes Kubernetes manifests and practical guidance for observability/logging.

## Tech Stack
- GitHub Actions
- Docker Hub
- Kubernetes (EKS)
- Trivy (DevSecOps scanning)
- Prometheus/Grafana (monitoring guidance)
- ELK (logging guidance)

## How deployment from GitHub Actions works
GitHub Actions needs kubeconfig credentials. The common approach is:
- Create a kubeconfig for a limited IAM identity (or service account)
- Store it as a GitHub Secret (base64 encoded)
- Pipeline decodes it and runs `kubectl apply`

### Required GitHub Secrets
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `KUBE_CONFIG_DATA`  (base64 encoded kubeconfig)

Encode your kubeconfig:
```bash
cat ~/.kube/config | base64 -w 0
```
Paste the output into GitHub Secrets as `KUBE_CONFIG_DATA`.

## Quick start
1) Update image name in `k8s/deployment.yaml`
2) Push to `main`
3) Pipeline runs automatically

## Manual deploy (optional)
```bash
kubectl apply -f k8s/
kubectl rollout status deploy/sample-app -n platform
kubectl get svc -n platform
```

## Notes
- For real production, you'd typically avoid long-lived kubeconfigs and use short-lived credentials (OIDC).
- This repo keeps it straightforward for portfolio purposes.
