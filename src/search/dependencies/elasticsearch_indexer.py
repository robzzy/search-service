# -*- coding: utf-8 -*-

from elasticsearch import NotFoundError

from search.dependencies.elasticsearch import ElasticsearchDependencyProvider
from search.documents.autocomplete import Autocomplete
from search.indexes.autocomplete import create_autocomplete_index, INDEX

class ElasticsearchIndexerApiWrapperBase:
    def __init__(self, client) -> None:
        self.client = client

    def get_document_by_id(self, index, doc_type, es_id):
        return doc_type.get(es_id, index=index)
    
    def save_document(self, doc_type, index, fields, es_id):
        doc_type(**fields, meta={"id": es_id}).save(index=index)
    
    def update_document(self, doc_type, index, fields, es_id):
        doc_type(meta={"id": es_id}).update(**fields, index=index)
    
    def delete_document(self, doc_type, index, es_id):
        try:
            doc_type(meta={"id": es_id}).delete(index=index)
        except NotFoundError:
            pass

class ElasticsearchIndexer(ElasticsearchDependencyProvider):

    class ApiWrapper(ElasticsearchIndexerApiWrapperBase):

        def get_autocomplete(self, es_id):
            return self.get_document_by_id(INDEX, Autocomplete, es_id)
    
    def setup(self):
        super(ElasticsearchIndexer, self).setup()
        create_autocomplete_index()
    
    def get_dependency(self, worker_ctx):
        return ElasticsearchIndexer.ApiWrapper(self.client)
