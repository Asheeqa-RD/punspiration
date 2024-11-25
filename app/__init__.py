from flask import Flask

def create_app(config_class='app.config.DevelopmentConfig'):
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
