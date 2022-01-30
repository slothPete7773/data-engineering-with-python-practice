import psycopg2 as db
import pandas as pd
conn_string="dbname='data_engineering_practice' host='localhost' user='slothpete' password='eNd76Kop3'"
conn=db.connect(conn_string)

# Query from db adapter -> dataframe
cur=conn.cursor()
query = "SELECT * FROM users"
cur.execute(query)

data = cur.fetchall()
df = pd.DataFrame(data)
print(df.head(5))
# Will only extract data from table, do not include table header; thus cause error in the below command.
# print(df['city'].value_counts())

# Query directy from pandas query function, though psycopg2 is not very much supported.
df = pd.read_sql("SELECT * FROM users", conn)
print(df.head(5))
print(df['city'].value_counts)
print(df['city'])
