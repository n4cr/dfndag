from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.python import PythonOperator
import pynautobot
import arrow


def simple_operation():
    print("Hello, World from a packaged dag!")
    print(pynautobot.api)
    res = arrow.get('2013-05-11T21:23:58.970460+07:00')

    print(res)


with DAG(
    "packaged_dag",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task1 = PythonOperator(task_id="task1", python_callable=simple_operation, dag=dag)

    task1
