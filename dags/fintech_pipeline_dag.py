"""
Orchestrates the PySpark MDM job, followed by Snowflake data quality checks, 
and dbt dimensional modeling.
"""
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('fintech_risk_pipeline', schedule_interval='@daily', start_date=datetime(2026, 9, 1)) as dag:

    # 1. Run PySpark Identity Resolution (MDM)
    run_mdm_spark_job = SparkSubmitOperator(
        task_id='run_pyspark_mdm',
        application='/jobs/identity_resolution.py',
        name='member_identity_resolution'
    )

    # 2. Run dbt to build the dimensional models in Snowflake
    run_dbt_models = BashOperator(
        task_id='dbt_run_risk_models',
        bash_command='dbt run --models tag:risk_analytics --profiles-dir /dbt'
    )

    # 3. Test for data quality and PII compliance
    test_dbt_models = BashOperator(
        task_id='dbt_test',
        bash_command='dbt test'
    )
        run_mdm_spark_job >> run_dbt_models >> test_dbt_models
