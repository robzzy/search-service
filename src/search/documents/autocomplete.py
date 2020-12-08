# -*- coding: utf-8 -*-

from elasticsearch_dsl import (
    Document,
    Keyword,
    Text,
    MetaField
)
from elasticsearch_dsl.field import Integer

from search.indexes.analyzers import autocomplete_analyzer


class Autocomplete(Document):

    class Meta:
        all = MetaField(enabled=False)
        dynamic = MetaField("strict")
    
    _dtype = Keyword()
    _dtype_id = Integer()

    autocomplete = Text(analyzer=autocomplete_analyzer)