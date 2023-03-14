#!/bin/sh

# add env variables to cds.yaml
cp /work/envoy-config/cds.yaml /work/envoy-config/_cds.yaml
cat /work/envoy-config/_cds.yaml | envsubst \$ENVOY_LB_ALG,\$TIMEOUT > /work/envoy-config/cds.yaml
rm /work/envoy-config/_cds.yaml

# add env variables to lds.yaml
cp /work/envoy-config/lds.yaml /work/envoy-config/_lds.yaml
cat /work/envoy-config/_lds.yaml | envsubst \$ENVOY_LB_ALG,\$TIMEOUT > /work/envoy-config/lds.yaml
rm /work/envoy-config/_lds.yaml

# Start Envoy
envoy -c /work/envoy-config/config.yaml -l debug 2> /tmp/envoy.log &

# Start Flask App
cd /work/app
gunicorn -w 3 -b 0.0.0.0 main:app