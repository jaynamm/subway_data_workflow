import json
import pathlib

import requests
import requests.exceptions as requests_exceptions

import airflow
from airflow import DAG
from airflow.operator.bash import BashOperator
from airflow.operator.python import PythonOperator

dag = DAG(
    dag_id = "collect_subway_congestion",
    start_date = airflow.utils.dates.days_ago(14),
    schedule_internal = None,
)

collect_subway_congestion = BashOperator(
    task_id = "collect-subway-congestion",
    bash_command = 'curl -o /Users/jaynam/workspace/airflow/data/subway_data \
        -X GET "https://api.odcloud.kr/api/15071311/v1/uddi:b3803d43-ffe3-4d17-9024-fd6cfa37c284?page=1&perPage=2000&serviceKey=su2fr9tzcPJq%2BBgU%2BcSme24%2Bh06u09KDlAsz6vXctNipdtX6EgkJSo3l1VCZWib8IB8rSlRc%2BQIeAz0ScidZDg%3D%3D" \
        -H  "accept: application/json" \
        -H  "Authorization: su2fr9tzcPJq+BgU+cSme24+h06u09KDlAsz6vXctNipdtX6EgkJSo3l1VCZWib8IB8rSlRc+QIeAz0ScidZDg=="',
    dag = dag,
    # env: Optional[Dict[str, str]] = None,
    # output_encoding: str = 'utf-8',
    # skip_exit_code: int = 99,
)


collect_subway_congestion