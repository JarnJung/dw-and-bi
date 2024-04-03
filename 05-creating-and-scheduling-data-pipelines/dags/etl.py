import glob
import json
import os
import logging

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils import timezone
from airflow.providers.postgres.hooks.postgres import PostgresHook

def _get_files(filepath):
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    logging.info(f"{num_files} files found in {filepath}")

    return all_files

def _create_tables():
    hook = PostgresHook(postgres_conn_id="my_postgres_conn")
    conn = hook.get_conn()
    cur = conn.cursor()

    table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
            id int,
            login text,
            PRIMARY KEY(id)
        )
    """
    table_create_events = """
        CREATE TABLE IF NOT EXISTS events (
            id text,
            type text,
            actor_id int,
            respo text,
            create_at text,
            PRIMARY KEY(id),
            CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
        )
    """

    create_table_queries = [
        table_create_actors,
        table_create_events,
    ]

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
    pass

def _process(**context):
    # Get list of files from filepath
    # all_files = get_files(filepath)

    hook = PostgresHook(postgres_conn_id="my_postgres_conn")
    conn = hook.get_conn()
    cur = conn.cursor()

    ti = context["ti"]
    all_files = ti.xcom_pull(task_ids="get_files", key = "return_value")

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                # Print some sample data
                
                if each["type"] == "IssueCommentEvent":
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                        each["payload"]["issue"]["url"],
                    )
                else:
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                    )

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO actors (
                        id,
                        login
                    ) VALUES ({each["actor"]["id"]}, '{each["actor"]["login"]}')
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO events (
                        id,
                        type,
                        respo,
                        actor_id,
                        create_at
                    ) VALUES ('{each["id"]}', '{each["type"]}', '{each["repo"]["name"]}', '{each["actor"]["id"]}', '{each["created_at"]}')
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                conn.commit()


with DAG (
    "etl",
    start_date= timezone.datetime(2024, 4, 3),
    schedule="@daily",
    tags=["DS525-DW"],
):
    start = EmptyOperator(task_id="start")

    get_files = PythonOperator(
        task_id="get_files",
        python_callable = _get_files,
        # op_args=["/opt/airflow/dags/data"],
        op_kwargs={
            "filepath":"/opt/airflow/dags/data",
        },
    )

    create_tables = PythonOperator(
        task_id="create_tables",
        python_callable = _create_tables,
    )

    process = PythonOperator(
        task_id="process",
        python_callable= _process,
    )

    stop = EmptyOperator(task_id="stop")

    start >> [get_files,create_tables] >> process >> stop




