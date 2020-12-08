# -*- coding: utf-8 -*-

import json

from nameko.rpc import rpc
from nameko.web.handlers import http
from nameko_tracer import Tracer

from search.dependencies.elasticsearch_indexer import ElasticsearchIndexer
from search.services.indexer.index_articles import ArticleIndexer


class IndexerService(ArticleIndexer):

    name = "indexer"
    tracer = Tracer()
    indexer = ElasticsearchIndexer()

    @http("GET", "/healthcheck")
    def health_check_http(self, request):
        return json.dumps(self.health_check())

    @rpc
    def health_check(self):
        return {"status": "ok"}
