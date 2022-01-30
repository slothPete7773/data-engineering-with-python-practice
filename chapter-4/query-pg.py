import psycopg2 as db
conn_string="dbname='data_engineering_practice' host='localhost' user='slothpete' password='eNd76Kop3'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "SELECT * FROM users"
cur.execute(query)

print(cur.fetchone())
print(cur.rowcount)
print(cur.rownumber)
print(cur.fetchmany(3))
print(cur.rownumber)
f=open('fromdb.csv','w')
conn=db.connect(conn_string)
cur=conn.cursor()
cur.copy_to(f,'users',sep=',')
f.close()
f=open('fromdb.csv','r')
print(f.read())


