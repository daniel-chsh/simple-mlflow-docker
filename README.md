# Description
Here is a quick way to deploy an MLflow server on a local or remote machine using Minio as s3 storage. You will first need to create a directory ```./buckets/mlflow```  
This can be done with the command ```mkdir -p buckets/mlflow```  

# Create your .env file
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
# To run
``` docker-compose --env-file ./.env up```  
The MLflow UI will be deployed on ```127.0.0.1:5000```  
# Run example
After starting the MLflow server - run ```python example.py```

