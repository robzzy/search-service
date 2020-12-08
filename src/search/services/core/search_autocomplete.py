# -*- coding: utf-8 -*-
from nameko.rpc import rpc


class AutocompleteMixin:
    @rpc
    def search_autocomplete(self, **search_params):
        hits = self.searcher("autocomplete-v1", **search_params).to_dict()["hits"][
            "hits"
        ]

        response = [hit["_source"] for hit in hits]

        return response
