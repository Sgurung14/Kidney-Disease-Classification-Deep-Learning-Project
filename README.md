# Kidney-Disease-Classification-Deep-Learning-Project

## Project Description

Kidney tumors are growths in the kidneys that can be benign or cancerous. Most do not cause symptoms, and are discovered unexpectedly when being diagnosed.

**This project aims to classify kidney tumors as benign or cancerous using machine learning techniques on Kidney CT Scan images.**

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
conda create -n kidney python=3.8 -y
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