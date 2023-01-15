import os
import pandas as pd

import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("daniel-test")

os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'http://127.0.0.1:5001'
os.environ['AWS_ACCESS_KEY_ID'] = 'minio'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'minio123'

if __name__=='__main__':
    random_state = 42

    X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=random_state)

    # splits data into 80% train 20% test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    # choose model with settings
    model = RandomForestClassifier(n_estimators=100) 
    model.fit(X_train, y_train)

    # define and print
    metrics = {"train_score": model.score(X_train, y_train), 
    "test_score": model.score(X_test, y_test)}

    # log params to mlflow and artifacts to minio
    mlflow.log_params({"n_estimators":100})
    mlflow.log_metrics(metrics)
    mlflow.sklearn.log_model(model, "rf-regressor")