### Build the container environment
```bash
docker build . -t cleaning
```
### Run the project with env file
```bash
docker run --env-file ./.env -d cleaning
```