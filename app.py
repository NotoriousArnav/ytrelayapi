from flask import Flask, jsonify

def create_app(*args,**kwargs):
    from blueprints import blueprints
    app = Flask(__name__)

    for x in blueprints:
        app.register_blueprint(x)

    return app