# -*- coding: utf-8 -*-


def test_health_check(search_service):

    result = search_service.health_check()

    assert result == {"status": "ok"}
