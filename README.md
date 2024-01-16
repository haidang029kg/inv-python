# pet-store/inventory-api



## Getting Started

Download links:

SSH clone URL: ssh://git@git.jetbrains.space/hungnguyen14fe/pet-store/inventory-api.git

HTTPS clone URL: https://git.jetbrains.space/hungnguyen14fe/pet-store/inventory-api.git



These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

1. install python with version from .python-version
2. install poetry
    -> pip install poetry
3. poetry config to create virtual env inside the project directory
    -> poetry config virtualenvs.in-project true
4. active poetry shell
    -> poetry shell
5. install packages
    -> poetry install
6. active venv
    -> source .venv/bin/activate
    
7. start server options
    a. start server FastAPI
        -> make server-fastapi

    b. start server gRPC
        -> make server-grpc

## Deployment

Add additional notes about how to deploy this on a production system.

## Resources

Add links to external resources for this project, such as CI server, bug tracker, etc.
