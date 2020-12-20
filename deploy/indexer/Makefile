
COMPONENT := indexer

-include common.mk

run:
	nameko run --config config.yaml search.services.$(COMPONENT).service:IndexerService

.PHONY: etc

ENV ?= default
TAG ?= $(shell git rev-parse HEAD)
REMOTE_DOCKER_HOST ?= zengzhiyuan

SERVICE_NAME := search-service

# docker
build-image:
	docker build -t $(SERVICE_NAME)-$(COMPONENT):$(TAG) .;

docker-tag:
	docker tag $(SERVICE_NAME)-$(COMPONENT):$(TAG) $(REMOTE_DOCKER_HOST)/$(SERVICE_NAME)-$(COMPONENT):$(TAG)

docker-push:
	docker push $(REMOTE_DOCKER_HOST)/$(SERVICE_NAME)-$(COMPONENT):$(TAG)
