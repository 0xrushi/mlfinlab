# Specify the name of the image
IMAGE_NAME = "mlfinlabstuf"

# Specify the path to the Dockerfile
DOCKERFILE_PATH = "."

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) $(DOCKERFILE_PATH)

# Run the Docker image
run:
	docker run --rm -it  -v ${PWD}:/work -p 8890:8890 $(IMAGE_NAME)

# Run the Docker image
runshell:
	docker run --rm -it  -v ${PWD}:/work -p 8890:8890 $(IMAGE_NAME) /bin/bash