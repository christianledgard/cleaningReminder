# Build the container environment
$ docker build . -t cleaning

# Run the project with env file
$ docker run --env-file ./.env -d cleaning