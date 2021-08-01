# For pre-process data for map reduce use
from pymongo import MongoClient

client = MongoClient('mongodb://10.0.0.22:27017/')
db = client.search_engine
collection = db.pokemon3

tr = open('pokemon_links.txt', 'w')
pr = open('pokemon_weights', 'w')

for doc in collection.find({}, {"url": 1, "links": 1}):
    url = doc.get('url', '')
    valid_links = []
    links_set = set(doc.get('links', [])) - set(url)
    valid_docs = collection.find({
        'url': {'$in': list(links_set)}
    })

    for doc in valid_docs:
        link = doc.get('url', '')
        valid_links.append(link)

    if url and valid_links:
        links_field = ' '.join(valid_links)
        line = url + '\t' + links_field + '\n'
        weight = url + '\t1.0\n'
        tr.write(line)
        pr.write(weight)

tr.close()
pr.close()
