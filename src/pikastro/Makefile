IMAGE_NAME = pikastro-api
IMAGE_VERSION = latest
DOCKER_REPO = europe-west4-docker.pkg.dev/pikastro-sandbox/pikastro/$(IMAGE_NAME)
PLATFORM = linux/amd64

.PHONY: build tag push run stop_container

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
	gcloud run deploy $(IMAGE_NAME)-sandbox --image $(DOCKER_REPO):$(IMAGE_VERSION) --platform managed --region europe-west4 --allow-unauthenticated --set-env-vars "ENVIRONMENT=development"


generate-docs: stop_container install_converter build
	# set environment variable ENVIRONMENT=development
	# run in detached mode
	docker run --env ENVIRONMENT=development -d -p 8080:8080 $(IMAGE_NAME):$(IMAGE_VERSION)
	api-spec-converter --from=openapi_3 --to=swagger_2 --syntax=yaml http://localhost:8080/openapi.json > openapi.yaml 
	docker stop $$(docker ps -qf 'ancestor=$(IMAGE_NAME)')

install_converter:
    # Check if api-spec-converter is installed
    ifeq (,$(shell which api-spec-converter))
        @echo "Installing api-spec-converter..."
        npm install -g api-spec-converter
    else
		@echo "api-spec-converter is already installed."
    endif

stop_container:
	@if [ -n "$$(docker ps -qf 'ancestor=$(IMAGE_NAME)')" ]; then \
		echo "Container defined"; \
		docker stop $$(docker ps -qf 'ancestor=$(IMAGE_NAME)'); \
	else \
		echo "Container not defined"; \
	fi

generate-api-config:
	gcloud api-gateway api-configs create solar-api-config \
  --api=solar-api --openapi-spec=openapi.yaml \
  --project=pikastro-sandbox --backend-auth-service-account=738779622748-compute@developer.gserviceaccount.com

deploy-api-gateway:
	gcloud api-gateway gateways create solar-gateway \
	--api=solar-api --api-config=solar-api-config \
	--location=europe-west2 --project=pikastro-sandbox