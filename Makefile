.PHONY: help build shell run test clean apply

help:
	@echo "Usage:"
	@echo "  make build      Build the Docker image"
	@echo "  make run        Run the container (executes default CMD)"
	@echo "  make shell      Run an interactive shell inside the container"
	@echo "  make test       Run tests with coverage"
	@echo "  make apply      Run the interest application job manually"
	@echo "  make clean      Remove Docker image"

build:
	docker build -t interest-account .

run:
	docker run --rm interest-account

shell:
	docker run --rm -it interest-account /bin/bash

test:
	docker run --rm interest-account pytest --cov=interest_account --cov-report=term-missing

apply:
	docker run --rm interest-account python /app/scripts/apply_interest_job.py

clean:
	docker rmi interest-account || true
