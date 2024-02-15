from flask import Flask, jsonify
from flask_cors import CORS

def list_routes(app):
    output = {}
    rules = list(app.url_map.iter_rules())
    funcs = list(app.view_functions.items())

    for x,y in zip(rules, funcs):
        out = {
            y[0]:{
                    'route':str(x),
                    'doc':y[1].__doc__
                }
        }
        output.update(out)
    return output
    

def create_app(*args,**kwargs):
    from blueprints import blueprints
    app = Flask(__name__)
    CORS(app)
    for x in blueprints:
        app.register_blueprint(x)

    @app.after_request 
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Accept-Ranges'] = 'bytes'
        # Other headers can be added here if needed
        return response

    @app.route('/')
    def index():
        """Index Route to List all available routes with their documentation"""
        return jsonify(
            list_routes(app)
        )

    return app