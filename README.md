## Directory Structure
- **app** - python app listening on port 8000
- **envoy-config** - envoy dynamic config files
- **scripts** - installation scripts used in docker build

## Docker Build

Build using the following
```
docker build -t flaskenvoy .
```

Run using the following
```
docker run -d -p 8000:8000 -p 8080:8080 flaskenvoy
```

## Container Structure

- All files are added to the `/work` directory
- Envoy log is written to `/tmp/envoy.log`