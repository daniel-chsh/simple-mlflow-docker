# Description
Here is a quick way to deploy an MLflow server on a local or remote machine using Minio as s3 storage.

# Install

```
git clone https://github.com/daniel-chsh/simple-mlflow-docker.git  # clone
cd simple-mlflow-docker
pip install -r requirements.txt  # install
```

# Create your own .env file or use the default
In the environment file you can change the values of the variables to the data you want. 
Required parameters:  
_____
MINIO_ACCESS_KEY=minio  
MINIO_SECRET_KEY=minio123  

MYSQL_DATABASE=mlflow  
MYSQL_USER=mlflow-user  
MYSQL_PASSWORD=mlflow-pass  
MYSQL_ROOT_PASSWORD=my-secret-pw  
____
# Run MLflow
```docker-compose --env-file ./.env up -d```  
The MLflow UI will be deployed on ```127.0.0.1:5000```  
# Run example
After starting the MLflow server - run ```python example.py```

