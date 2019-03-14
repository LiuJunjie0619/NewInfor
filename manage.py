# -*- encoding: utf-8 -*-
from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config.config_dict['config'])


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
