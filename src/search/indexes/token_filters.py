# -*- coding: utf-8 -*-

from elasticsearch_dsl import token_filter

autocomplete_filter = token_filter(
    "autocomplete_filter", type="edge_ngram", min_gram=1, max_gram=20
)
