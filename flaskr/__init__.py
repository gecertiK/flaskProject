import os

from flask import Flask, request
from faker import Faker
import pandas as pd
import requests
from flaskr.db import get_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

############################################PART_2_WORK_WITH_SQL#######################################
    from . import db
    db.init_app(app)

    from . import select_tracks
    app.register_blueprint(select_tracks.bp)

    from . import app_parse
    app.register_blueprint(app_parse.bp)

    return app
