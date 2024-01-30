# pet-store/python-api

## Getting Started

Download links:

SSH clone URL: ssh://git@git.jetbrains.space/hungnguyen14fe/pet-store/python-api.git

HTTPS clone URL: <https://git.jetbrains.space/hungnguyen14fe/pet-store/python-api.git>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

Follow these steps to set up your environment:

1. **Install Python**: Use the version specified in the `.python-version` file.

2. **Install Poetry**: Poetry is a dependency management tool for Python. Install it with pip:

    ```bash
    pip install poetry
    ```

3. **Configure Poetry**: Set Poetry to create the virtual environment inside the project directory:

    ```bash
    poetry config virtualenvs.in-project true
    ```

4. **Activate Poetry Shell**: This will create a new shell within the virtual environment:

    ```bash
    poetry shell
    ```

5. **Install Packages**: Install the necessary packages using Poetry:

    ```bash
    poetry install
    ```

6. **Activate Virtual Environment**: Activate the virtual environment created by Poetry:

    ```bash
    source .venv/bin/activate
    ```

7. **Start Server**: You have two options to start the server:

    a. **FastAPI Server**:

        ```bash
        make server-fastapi
        ```

    b. **gRPC Server**:

        ```bash
        make server-grpc
        ```

## Deployment

Add additional notes about how to deploy this on a production system.

## Resources

Add links to external resources for this project, such as CI server, bug tracker, etc.
