# -*- coding: utf-8 -*-


from search.dependencies.elasticsearch import ElasticsearchDependencyProvider


class ElasticsearchSearcherApiWrapperBase:
    def __init__(self, client) -> None:
        self.client = client

    def find(self):
        pass


class ElasticsearchSearcher(ElasticsearchDependencyProvider):
    class ApiWrapper(ElasticsearchSearcherApiWrapperBase):

        pass

    def setup(self):
        return super().setup()

    def get_dependency(self, worker_ctx):
        return self.ApiWrapper(self.client).find
