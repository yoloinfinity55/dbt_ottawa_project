from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'dbt_snowflake_production_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    run_dbt = BashOperator(
        task_id='run_and_test_dbt_models',
        bash_command='./run_production_pipeline.sh'
    )
