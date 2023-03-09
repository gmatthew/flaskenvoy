import os

from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

ENVIRONMENT = Environment(loader=FileSystemLoader("templates/"))
TEMPLATE = ENVIRONMENT.get_template("eds.jinja")

OUTPUT_ENVOY_CONFIG_PATH = "/work/envoy-config/eds.yaml"

@app.route("/")
def hello():
  endpoints_args = request.args["endpoints"]
  endpoints = endpoints_args.split(",")
  
  rendered_template = TEMPLATE.render(endpoints=endpoints)

  write_results(rendered_template)

  return rendered_template

# writes first choice node and container name to results file
def write_results(template):
  tmp_output = "/tmp/fetcher-temp.yaml"

  f = open(tmp_output, "w")
  f.write(template)
  f.close()

  os.system('mv -f ' + tmp_output + " " + OUTPUT_ENVOY_CONFIG_PATH)