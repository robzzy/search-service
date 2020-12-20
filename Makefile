.PHONY: run
run-search:
	make -C deploy/core run

run-indexer:
	make -C deploy/indexer run


.PHONY: test

#  vars
ifdef CIRCLE_SHA1
TAG ?=$(CIRCLE_SHA1)
else
TAG ?= $(shell git rev-parse HEAD)
endif

HTMLCOV_DIR ?= htmlcov
IMAGES := core indexer

CONTEXT ?= minikube
NAMESPACE ?= default
RELEASE_NAME := search-service
CHART_FOLDER_NAME ?= search-service
PROJECT_DOCKER_HOST ?= zengzhiyuan

DB_REVISION ?= head

install-dependencies:
	pip install -U -e ".[dev]"


# test
coverage-html:
	coverage html -d $(HTMLCOV_DIR)

coverage-report:
	coverage report -m

test:
	flake8 src test
	coverage run --concurrency=eventlet --source=search -m pytest test $(ARGS)

coverage: test coverage-report coverage-html


# docker
clean-source:
	docker rm source || true

docker-build-wheel: clean-source
	docker create -v /application -v /wheelhouse --name source alpine:3.4
	docker cp . source:/application
	docker run --rm --volumes-from source $(PROJECT_DOCKER_HOST)/python-builder:latest;
	docker cp source:/wheelhouse .
	docker rm source

build-base: docker-build-wheel
	docker pull $(PROJECT_DOCKER_HOST)/python-base:latest
	docker tag $(PROJECT_DOCKER_HOST)/python-base:latest python-base:latest
	docker build -t search-base .

build: build-base
	for image in $(IMAGES) ; do TAG=$(TAG) make -C deploy/$$image build-image; done

docker-login:
	echo $$DOCKER_PASSWORD | docker login --username=$(DOCKER_USERNAME) --password-stdin

docker-save:
	docker save -o search-service.tar $(foreach image, $(IMAGES), search-service-$(image):$(TAG))

docker-load:
	docker load -i search-service.tar

docker-tag:
	for image in $(IMAGES); do make -C deploy/$$image docker-tag; done

push-images:
	for image in $(IMAGES); do make -C deploy/$$image docker-push; done


# k8s
# helm
test-chart:
	helm upgrade $(RELEASE_NAME) deploy/k8s/charts/$(CHART_FOLDER_NAME) --install \
	--namespace=$(NAMESPACE) --kube-context=$(CONTEXT) \
	--dry-run --debug \
	--set image.tag=$(TAG) \
	--set db_revision=$(DB_REVISION);

install-chart:
	helm upgrade search-service deploy/k8s/charts/$(CHART_FOLDER_NAME) --install \
	--namespace=$(NAMESPACE) --kube-context=$(CONTEXT) \
	--set image.tag=$(TAG) \
	--set run_migrations=$(RUN_MIGRATIONS) \
	--set db_revision=$(DB_REVISION);

lint-chart:
	helm lint deploy/k8s/charts/$(CHART_FOLDER_NAME) --strict
