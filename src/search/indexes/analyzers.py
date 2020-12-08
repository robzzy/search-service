# -*- coding: utf-8 -*-

from elasticsearch_dsl import analyzer
from .token_filters import autocomplete_filter

autocomplete_analyzer = analyzer(
    "autocomplete",
    type="custom",
    tokenizer="smartcn_tokenizer",
    filter=[autocomplete_filter, "lowercase"],
)
