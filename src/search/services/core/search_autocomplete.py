# -*- coding: utf-8 -*-
from nameko.rpc import rpc


class AutocompleteMixin:
    @rpc
    def search_autocomplete(self, **search_params):
        return self.searcher("autocomplete-v1", **search_params).to_dict()
