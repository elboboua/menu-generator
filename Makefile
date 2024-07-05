# Variables
APP_NAME=server
IMAGE_NAME=menu_generator_image
CONTAINER_NAME=menu_generator_container
DOCKERFILE=Containerfile
PORT=8000

# Default target
.PHONY: all
all: help

# Help target
.PHONY: help
help:
	@echo "Makefile for FastAPI project"
	@echo "Usage:"
	@echo "  make dev           - Run the app in development mode"
	@echo "  make build         - Build the Docker image"
	@echo "  make run           - Run the Docker container"
	@echo "  make stop          - Stop the Docker container"
	@echo "  make clean         - Remove Docker image and container"

# Run the app in development mode
.PHONY: dev
dev:
	fastapi dev $(APP_NAME).py

# Build the Docker image
.PHONY: image
image:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) .

# Run the Docker container
.PHONY: run
run:
	docker run -d --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

# Stop the Docker container
.PHONY: stop
stop:
	docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME)

# Clean up Docker image and container
.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME)
