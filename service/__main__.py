import os

import bottle

from config_finder import cfg

def env_handler():
    return dict(os.environ)

def cfg_handler(key):
    return {key: cfg(key)}


bottle.route("/", ["GET"], lambda: "Hello!")
bottle.route("/env", ["GET"], env_handler)
bottle.route("/cfg/:key", ["GET"], cfg_handler)

print("Running mock service")
bottle.run(host='0.0.0.0', port='8000', debut=True)

