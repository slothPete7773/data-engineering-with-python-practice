from operator import index
from elasticsearch import Elasticsearch

es = Elasticsearch() 

# doc = {"query": {"match_all": {}}}
# res = es.search(index='users', body=doc, size=10)
# print(res['hits']['hits'])

# # Get all the documents
# doc={"query":{"match_all":{}}}
# res=es.search(index="users",body=doc,size=10)
# print(res['hits']['hits'][9]['_source'])

doc={"query":{"bool":{"must":{"match":{"city":"South"}}}}}
res=es.search(index="users",body=doc,size=10)
print(res['hits']['hits'])