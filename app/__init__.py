from flask import Flask
from app.routes.routes import app_routes
from app.routes.text_search import text_search_routes
from app.routes.upload import upload_routes
from app.routes.browse import browse_routes
from app.routes.similarity  import similarity_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_routes)
    app.register_blueprint(browse_routes)
    app.register_blueprint(text_search_routes)
    app.register_blueprint(upload_routes)
    app.register_blueprint(similarity_routes)

    return app
