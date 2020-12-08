# -*- coding: utf-8 -*-

from elasticsearch_dsl import Index
from search.documents.autocomplete import Autocomplete
from search.indexes.analyzers import autocomplete_analyzer

INDEX_VERSION = 1
INDEX = f"autocomplete-v{INDEX_VERSION}"


def create_autocomplete_index():

    autocomplete = Index(INDEX)

    if autocomplete.exists():
        return autocomplete

    autocomplete.settings(number_of_shards=1, number_of_replicas=2)

    autocomplete.analyzer(autocomplete_analyzer)

    autocomplete.document(Autocomplete)

    autocomplete.create()

    return autocomplete
