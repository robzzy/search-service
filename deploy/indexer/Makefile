
COMPONENT := indexer

-include common.mk

run:
	nameko run --config config.yaml search.services.$(COMPONENT).service:IndexerService
