from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the exact command we want to run
# 1. Go into the project folder
# 2. Install deps (needed for fresh containers)
# 3. Run with explicit profile pointing to current dir (.)
# 4. Test with explicit profile pointing to current dir (.)
DBT_COMMAND = """
cd jaffle_shop && dbt deps && dbt run --profiles-dir . && dbt test --profiles-dir .
"""

with DAG(
    'dbt_snowflake_production_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    run_dbt = BashOperator(
        task_id='run_and_test_dbt_models',
        bash_command=DBT_COMMAND
    )
