#!/bin/sh

# Start Envoy
envoy -c /work/envoy-config/config.yaml -l debug 2> /tmp/envoy.log &

# Start Flask App
cd /work/app
gunicorn -w 3 -b 0.0.0.0 main:app