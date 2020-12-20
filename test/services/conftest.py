import pytest

from nameko.testing.services import worker_factory

from search.services.core.service import SearchService
from search.services.indexer.service import IndexerService


@pytest.fixture
def search_service():
    yield worker_factory(SearchService)


@pytest.fixture
def indexer_service():
    yield worker_factory(IndexerService)
