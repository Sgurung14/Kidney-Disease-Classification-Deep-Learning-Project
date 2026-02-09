# Kidney-Disease-Classification-Deep-Learning-Project

## Project Description

Kidney tumors are growths in the kidneys that can be benign or cancerous. Most do not cause symptoms, and are discovered unexpectedly when being diagnosed.

**This project aims to classify kidney tumors as benign or cancerous using machine learning techniques on Kidney CT Scan images.**

### Tech Stack  

| Layer | Technology |
|------|-----------|
| Language | Python |
| Data Versioning | DVC |
| Experiment Tracking | MLflow |
| Pipeline | DVC + Python scripts |
| Environment | Conda / pip |
| API Serving | Flask / FastAPI |
| CI/CD | GitHub Actions |
| Cloud | AWS EC2 |

---


## Preprocessing Pipeline

This project uses a lightweight, medically appropriate preprocessing pipeline tailored for **2D CT kidney images (JPG)** and **transfer learning**.

---


### 1. Image Resizing
Matches the input size expected by pretrained CNNs (e.g., ResNet, EfficientNet) and ensures consistent batching.



### 2. ImageNet Preprocessing
Aligns image intensity distribution with ImageNet-trained weights, enabling effective feature reuse and faster convergence.



### 3. Intensity Normalization  
Stabilizes training across scans from different hospitals, scanners, and contrast protocols.



### 4. Data Augmentation (Training Only)
Improves robustness to anatomical variation, scanner differences, and contrast variability while preserving anatomical realism.



### 5. No Vertical Flipping
Up–down flipping violates human anatomical orientation and degrades generalization in CT imaging.



### 6. Class Imbalance Handling
Ensures minority classes (tumor, stone) contribute proportionally to the loss, improving recall and balanced performance.

---

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml
9. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.11 -y
```

```bash
conda activate kidney
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/{username}/Kidney-Disease-Classification-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME={username} \
MLFLOW_TRACKING_PASSWORD={access token} \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/{username}/Kidney-Disease-Classification-MLflow-DVC.mlflow 

export MLFLOW_TRACKING_USERNAME={username}

export MLFLOW_TRACKING_PASSWORD={access token}

```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI, will be something like: 851459781228.dkr.ecr.us-east-1.amazonaws.com/kidney

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
