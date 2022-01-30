from elasticsearch import Elasticsearch
from faker import Faker

fake=Faker()
es = Elasticsearch() #or  Elasticsearch({127.0.0.1})

doc = {"name": fake.name(),"street": fake.street_address(), "city": fake.city(),"zip":fake.zipcode()}

# Index method let u add data.
result = es.index(index="users",doc_type="doc",body=doc)
print("===")
print(result)

doc2 = {"query":{"match":{"_id":"pDYlOHEBxMEH3Xr-2QPk"}}}
result2=es.search(index="users",body=doc2,size=10)
print("===")
print(result2)
