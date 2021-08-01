# Pokemon Search Engine

## Description

A search engine of pokemon wiki (https://bulbapedia.bulbagarden.net/wiki/Main_Page)

## Use PageRank to optimize search result

In default, each result has the same weight when you search them by any keywords. To get a result that makes more sense, we use PageRank to adjust the weight of each page:

* Run processor/data_pre_processor.py, two files will be generated: pokemon_links and pokemon_weights.
* Run PageRank using these two files, finally we get the file pokemon_weight_30.
* Copy pokemon_weight_30 into processor folder, then run data_post_processor.py.

## Author

Jiaxin Wang