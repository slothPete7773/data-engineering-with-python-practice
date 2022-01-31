import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd

def cleanScooter():
    df=pd.read_csv('/home/slothpete/Desktop/programming/data-engineer-practice/my-source/chapter-5/scooter.csv')
    df.drop(columns=['region_id'], inplace=True)
    df.columns=[x.lower() for x in df.columns]
    df['started_at']=pd.to_datetime(df['started_at'],format='%m/%d/%Y %H:%M')
    df.to_csv('/home/slothpete/Desktop/programming/data-engineer-practice/my-source/chapter-5/airflow-output/cleanscooter.csv')


def filterData():
    df=pd.read_csv('/home/slothpete/Desktop/programming/data-engineer-practice/my-source/chapter-5/airflow-output/cleanscooter.csv')
    fromd = '2019-05-23'
    tod='2019-06-03'
    tofrom = df[(df['started_at']>fromd)&(df['started_at']<tod)]
    tofrom.to_csv('/home/slothpete/Desktop/programming/data-engineer-practice/my-source/chapter-5/airflow-output/may23-june3.csv')	


default_args = {
    'owner': 'slothPete',
    'start_date': dt.datetime(2020, 4, 13),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('Chapter-5-cleaning-data',
         default_args=default_args,
         schedule_interval='0 * * * *',      # 5 mins,
         ) as dag:

    cleanData = PythonOperator(task_id='clean',
                                 python_callable=cleanScooter)
    
    selectData = PythonOperator(task_id='filter',
                                 python_callable=filterData)

    moveFile = BashOperator(task_id='move',
                                 bash_command='cp /home/slothpete/Desktop/programming/data-engineer-practice/my-source/chapter-5/airflow-output/may23-june3.csv /home/slothpete/Desktop')



cleanData >> selectData >> moveFile
