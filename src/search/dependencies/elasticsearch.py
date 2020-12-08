# -*- coding: utf-8 -*-

from elasticsearch_dsl.connections import connections

from nameko import config
from nameko.extensions import DependencyProvider

ES_CONNECTION_TIMEOUT = 30
ES_DEFAULT_PAGE_NUMBER = 1
ES_DEFAULT_PAGE_SIZE = 10
ES_NO_PAGINATION = 10000


class ElasticsearchDependencyProvider(DependencyProvider):
    def setup(self):
        host = config.get("ELASTICSEARCH_URI")
        self.client = connections.create_connection(
            hosts=[host], timeout=ES_CONNECTION_TIMEOUT, retry_on_timeout=True,
        )

    def get_dependency(self, worker_ctx):
        raise NotImplementedError()
