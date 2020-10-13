.PHONY: all test build push

all: test build push
VERSION := "1.0"

test: 
	python -m pytest 

build: 
	docker build -t vallard/root-canal:${VERSION} . 

push: 
	docker push vallard/root-canal:${VERSION}

