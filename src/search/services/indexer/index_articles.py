# -*- coding: utf-8 -*-

from nameko.events import event_handler


class ArticleIndexer:
    @event_handler("articles", "article_created")
    def handle_article_created(self, payload):
        print(payload)

    @event_handler("articles", "author_created")
    def handle_author_created(self, payload):
        print(payload)
