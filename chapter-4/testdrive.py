import psycopg2 as db
conn_string="dbname='data_engineering_practice' host='localhost' user='slothpete' password='eNd76Kop3'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "insert into users (id,name,street,city,zip) values({},'{}','{}','{}','{}')".format(1,'Big Bird','Sesame Street','Fakeville','12345')
print("1st SQL formatted command: ")
print(cur.mogrify(query))
print('===')

query2 = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"
data=(1,'Big Bird','Sesame Street','Fakeville','12345')
print("2nd SQL cformatted ommand: ")
print(cur.mogrify(query2,data))
print('===')
# cur.execute(query2,data)
# conn.commit()



