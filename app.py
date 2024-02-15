from flask import Flask, jsonify

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

    for x in blueprints:
        app.register_blueprint(x)

    @app.route('/')
    def index():
        """Index Route to List all available routes with their documentation"""
        return jsonify(
            list_routes(app)
        )

    return app