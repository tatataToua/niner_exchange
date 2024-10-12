from .auth import auth_bp
from .user import user_bp
from .listing import listing_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(listing_bp)