import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch, helpers

def queryPostgresql():
    conn_string="dbname='data_engineering_practice' host='localhost' user='slothpete' password='eNd76Kop3'"
    conn=db.connect(conn_string)
    df=pd.read_sql("SELECT name,city FROM users",conn)
    df.to_csv('/home/slothpete/Desktop/programming/data-engineer-practice/my-source/postgresqldata-fromAirflow.csv')
    print("-------Data Saved------")

def insertElasticsearch():
    es = Elasticsearch() 
    df=pd.read_csv('/home/slothpete/Desktop/programming/data-engineer-practice/my-source/postgresqldata-fromAirflow.csv')
    for i,r in df.iterrows():
        doc=r.to_json()
        res=es.index(index="frompostgresql",doc_type="doc",body=doc)
        print(res)
    	
default_args = {
    'owner': 'slothpete',
    'start_date': dt.datetime(2020, 4, 2),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('Chapter4-DAG-ConnectingDB',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    getData = PythonOperator(task_id='QueryPostgreSQL',
                                 python_callable=queryPostgresql)
    
    insertData = PythonOperator(task_id='InsertDataElasticsearch',
                                 python_callable=insertElasticsearch)

getData >> insertData
