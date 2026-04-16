import dagshub
dagshub.init(repo_owner='BadalKumarSahoo20', repo_name='mlproject', mlflow=True)

import mlflow

with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)