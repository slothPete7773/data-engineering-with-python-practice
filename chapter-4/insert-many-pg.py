import psycopg2 as db
from faker import Faker
fake = Faker()
data = []
i = 2
for r in range(1000):
    data.append((i,fake.name(),fake.street_address(), fake.city(),fake.zipcode()))
    i+=1
data_for_db=tuple(data)
print(data_for_db)

conn_string="dbname='data_engineering_practice' host='localhost' user='slothpete' password='eNd76Kop3'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "INSERT INTO users (id,name,street,city,zip) VALUES(%s,%s,%s,%s,%s)"
print(cur.mogrify(query,data_for_db[1]))

cur.executemany(query,data_for_db)
conn.commit()

query2 = "SELECT * FROM users"

cur.execute(query2)
print(cur.fetchall())
