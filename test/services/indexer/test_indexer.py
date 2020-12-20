# -*- coding: utf-8 -*-


def test_health_check(indexer_service):

    result = indexer_service.health_check()

    assert result == {"status": "ok"}
