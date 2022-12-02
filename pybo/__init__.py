from flask import Flask
import pybo.config.app_config as conf

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(conf)

    from .views import main_views, user_views, music_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_views.bp)
    app.register_blueprint(music_views.bp)

    return app