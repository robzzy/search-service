# -*- coding: utf-8 -*-

from nameko.events import event_handler
from elasticsearch import NotFoundError


class ArticleIndexer:
    @event_handler("articles", "article_created")
    def handle_article_created(self, payload):
        article = payload["article"]

        data = {
            "_dtype_id": article["id"],
            "_dtype": "article",
            "autocomplete": article["title"]
        }

        try:
            self.indexer.update_autocomplete(data)
        except NotFoundError:
            self.indexer.create_autocomplete(data)

    @event_handler("articles", "author_created")
    def handle_author_created(self, payload):
        author = payload["author"]

        data = {
            "_dtype_id": author["id"],
            "_dtype": "author",
            "autocomplete": author["nickname"]
        }

        try:
            self.indexer.update_autocomplete(data)
        except NotFoundError:
            self.indexer.create_autocomplete(data)
