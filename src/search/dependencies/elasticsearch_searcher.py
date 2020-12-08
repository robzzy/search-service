# -*- coding: utf-8 -*-

from elasticsearch_dsl import Search, Q

from search.dependencies.elasticsearch import ElasticsearchDependencyProvider


class ElasticsearchSearcherApiWrapperBase:
    def __init__(self, client) -> None:
        self.client = client
        self.search = None

    def _apply_queries(self, index, **kwargs):
        raise NotImplementedError()

    def find(self, index, **kwargs):
        self.search = Search(using=self.client, index=index).sort(
            {"_score": {"order": "desc"}}
        )
        queries = self._apply_queries(index, **kwargs)

        searcher = self.search.query(queries)

        return searcher.execute()


class ElasticsearchSearcher(ElasticsearchDependencyProvider):
    class ApiWrapper(ElasticsearchSearcherApiWrapperBase):
        def _apply_queries(self, index, **kwargs):
            term = kwargs.get("term")

            should = [Q("match_all")]

            if term:

                match_query = Q("match", autocomplete=term)
                should.append(match_query)

                phrase_query = Q("match_phrase", autocomplete=term)
                should.append(phrase_query)

            queries = Q("bool", should=should)

            return queries

    def setup(self):
        return super().setup()

    def get_dependency(self, worker_ctx):
        return self.ApiWrapper(self.client).find
