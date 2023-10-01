# Variables
PROTOC = protoc
PROTO_DIR = ./protos
PROTO_FILES = $(wildcard $(PROTO_DIR)/*.proto)
PROTO_OUT_DIR = ./generated

# Targets
.PHONY: grpc-inventory

grpc-server-inventory:
	python inventory_server.py

grpc-inventory:
	python -m grpc_tools.protoc -I./protos --mypy_out=$(PROTO_OUT_DIR) --python_out=$(PROTO_OUT_DIR) --grpc_python_out=$(PROTO_OUT_DIR) $(PROTO_FILES)

aerich-init:
	aerich init -t app.settings.TORTOISE_ORM --location app/models/migrations