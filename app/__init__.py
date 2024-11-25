from flask import Flask, jsonify

def create_app(config_class='app.config.DevelopmentConfig'):
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"status":"error","message":"Resource not found"}),404

    # Register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
