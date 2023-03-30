import os

from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

ENVIRONMENT = Environment(loader=FileSystemLoader("templates/"))
TEMPLATE = ENVIRONMENT.get_template("destination-rule.jinja")
OUTPUT_ENVOY_CONFIG_PATH = "/home/ubuntu/experiment-tools/configs/"

@app.route("/")
def hello():
  max_conn = request.args["max_conn"]
  requests = request.args["requests"]
  service = request.args["service"]
  

  # Render the template
  rendered_template = TEMPLATE.render(max_conn=max_conn, requests=requests, service=service)
  write_results(service, rendered_template)

  # Update Kubernetes
  os.system('kubectl apply -f ' + OUTPUT_ENVOY_CONFIG_PATH )

  return rendered_template


# writes first choice node and container name to results file
def write_results(service, template):
  tmp_output = "/tmp/{0}-destination-rule.yaml".format(service)

  f = open(tmp_output, "w")
  f.write(template)
  f.close()

  os.system('mv -f ' + tmp_output + " " + OUTPUT_ENVOY_CONFIG_PATH)