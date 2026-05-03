from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("/opt/project")

from main import run_pipeline


def run_etl():
    run_pipeline()


default_args = {
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="weather_pipeline",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    run_pipeline_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_etl,
    )
