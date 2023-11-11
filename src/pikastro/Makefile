IMAGE_NAME = pikastro-api
IMAGE_VERSION = latest
DOCKER_REPO = europe-west4-docker.pkg.dev/pikastro-sandbox/pikastro/$(IMAGE_NAME)
PLATFORM = linux/amd64

.PHONY: build tag push run

configure:
	gcloud auth configure-docker europe-west4-docker.pkg.dev

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_VERSION) .

tag: build
	docker tag $(IMAGE_NAME):$(IMAGE_VERSION) $(DOCKER_REPO):$(IMAGE_VERSION)

push: tag
	docker push $(DOCKER_REPO):$(IMAGE_VERSION)

run:
	docker run -p 8080:8080 $(IMAGE_NAME):$(IMAGE_VERSION)

deploy: push
	gcloud run deploy $(IMAGE_NAME)-sandbox --image $(DOCKER_REPO):$(IMAGE_VERSION) --platform managed --region europe-west4 --allow-unauthenticated