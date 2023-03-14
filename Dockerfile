FROM --platform=linux/amd64 ubuntu:latest

WORKDIR /work

# # Flask
# EXPOSE 8000/tcp 
# # Envoy
# EXPOSE 8080/tcp

COPY ./ /work

RUN sh /work/scripts/install-envoy.sh
RUN sh /work/scripts/install-flask.sh

# Start Envoy
ENTRYPOINT [ "sh", "/work/scripts/start.sh" ] 
