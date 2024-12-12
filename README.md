# CLIP_vectorization_bentoML

BentoML Service for CLIP Image Vectorization, built using BentoML and pushed to ECR.

Ideally I would use Github Actions here, however the model is too big for the storage space provided. I could make a private Runner but its a bit overkill right now for this small project, so pushing from the CLI.

## Local install

1. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   python3 -m pip install transformers Pillow torch bentoml
   ```

## Run Local Service

1. Start the BentoML service:
   ```bash
   bentoml serve service:vectorization
   ```
2. Verify the service is running:
   - Health Check:
     ```bash
     curl -v http://127.0.0.1:3000/livez
     ```
   - Metrics:
     ```bash
     curl http://127.0.0.1:3000/metrics
     ```

---


## Build a BentoML container image

```
# Use Bento to make a container image
bentoml build

# Re tag the image so it isn't random
bentoml containerize clip_image_vectorizer:latest -t bentoml:latest
```

### Run the container locally

```
docker run --rm -p 3000:3000 bentoml:latest
```

### Push to ECR and Verify

```
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $REPO_URI

docker tag bentoml:latest 016230046494.dkr.ecr.eu-west-1.amazonaws.com/quickvectors-repository:bentoml-latest

docker push 016230046494.dkr.ecr.eu-west-1.amazonaws.com/quickvectors-repository:bentoml-latest

# Verify
aws ecr list-images --repository-name quickvectors-repository
```
