import psycopg2 as db
conn_string="dbname='data_engineering_practice' host='localhost' user='slothpete' password='eNd76Kop3'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "SELECT * FROM users"
cur.execute(query)
# for item in cur:
#     print(item)
# print("===")

print(cur.fetchone())
print("===")

print(cur.fetchmany(5))
print("===")

print(cur.fetchmany(5))
print("===")

data = cur.fetchall()
print(data[9])
print(data[10])

# Exporting to csv file with psycopg2's built-in export tooll
file = open('fromodb.csv', 'w')
cur.copy_to(file, 'users', sep=',')
file.close