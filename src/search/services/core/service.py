# -*- coding: utf-8 -*-

import json

from nameko.rpc import rpc
from nameko.web.handlers import http
from nameko_tracer import Tracer

from search.dependencies.elasticsearch_searcher import ElasticsearchSearcher
from search.services.core.search_autocomplete import AutocompleteMixin


class SearchService(AutocompleteMixin):

    name = "search"
    tracer = Tracer()
    searcher = ElasticsearchSearcher()

    @http("GET", "/healthcheck")
    def health_check_http(self, request):
        return json.dumps(self.health_check())

    @rpc
    def health_check(self):
        return {"status": "ok"}
