import os


def check_docker_environment():
    return os.getenv("DOCKER", "False").lower() == "true"
