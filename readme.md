# Deploying Containerized App to Cloud Run using Artifact Registry

## Prerequisites
- Google Cloud SDK installed
- Docker installed
- Google Cloud Project configured
- Containerized application ready

## 1. Authentication and Project Setup
```bash
# Authenticate with Google Cloud
gcloud auth login

# Set the project
gcloud config set project YOUR_PROJECT_ID
```

## 2. Docker Authentication for Artifact Registry
```bash
# Get access token
 gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://us-central1-docker.pkg.dev
```

## 3. Create Artifact Registry Repository
```bash
# Create a repository in Artifact Registry
gcloud artifacts repositories create REPO_NAME \
    --repository-format=docker \
    --location=REGION \
    --description="Docker repository"
```

## 4. Build and Tag Docker Image
```bash
# Build your Docker image
docker build -t us-central1-docker.pkg.dev/emerald-entity-442316-d6/my-flask-repo/app:1

# Push image to Artifact Registry
sudo docker push  us-central1-docker.pkg.dev/emerald-entity-442316-d6/my-flask-repo/app:1
```

## 5. Deploy to Cloud Run
```bash
# Deploy the containerized application
gcloud run deploy trail-app \
    --image=--image=us-central1-docker.pkg.dev/emerald-entity-442316-d6/my-flask-repo/app:1 \
    --allow-unauthenticated \
    --port=8080 \
    --region=us-central1 \
    --project=emerald-entity-442316-d6
```

## 6. Verify Deployment
```bash
# List deployed Cloud Run services
gcloud run services list


```

## Common Variables to Replace
- `YOUR_PROJECT_ID`: Your Google Cloud Project ID
- `REGION`: Your preferred Google Cloud region (e.g., us-central1)
- `REPO_NAME`: Name for your Artifact Registry repository
- `IMAGE_NAME`: Name for your Docker image
- `TAG`: Image version tag
- `SERVICE_NAME`: Name for your Cloud Run service
