# Updates weights of urls in Elasticsearch
import elasticsearch.exceptions
from elasticsearch_dsl.connections import connections

from processor.es_types import PokemonType

connections.create_connection(hosts=['localhost'])


with open('pokemon_weights_30', 'r') as weights:
    line = weights.readline()
    while line:
        line = line.rstrip('\n')
        print(line)
        url, weight = line.split('\t')
        try:
            entry = PokemonType.get(id=url, index='pokemon3')
            for single_suggest in entry.suggest:
                original_weight = single_suggest['weight']
                single_suggest['weight'] = int(single_suggest['weight'] * float(weight) * 10000)
            print(entry.suggest)
            entry.save()
        except elasticsearch.exceptions.NotFoundError:
            pass
        line = weights.readline()

