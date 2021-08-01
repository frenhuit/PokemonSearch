from elasticsearch_dsl import Document, Completion, Keyword, Text

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])


class PokemonType(Document):
    """Pokemon type used in Elasticsearch"""
    url = Keyword()
    title = Keyword()
    content = Text()
    links = Keyword()
    suggest = Completion()

    class Index:
        name = 'pokemon3'
        settings = {"number_of_shards": 3, "number_of_replicas": 1}
