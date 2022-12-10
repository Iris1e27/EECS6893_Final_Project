import os
from flask import Flask, abort, request, render_template, g, redirect, Response, Blueprint, url_for, session, flash
import functools

from werkzeug.security import check_password_hash, generate_password_hash
import time

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,template_folder=tmpl_dir)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.secret_key = "super secret key"
    app.run(host='0.0.0.0', port=8111)