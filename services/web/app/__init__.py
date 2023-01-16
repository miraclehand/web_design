from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import logging


db = SQLAlchemy()

def create_app():
    # apply configuration
    app = Flask(__name__)

    cfg = os.path.join('../', 'config', "development" + '.py')
    app.config.from_pyfile(cfg)

    db.init_app(app)

    from app.api.users import user_bp
    from app.api.customers import customer_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(customer_bp, url_prefix='/api/customers')

    return app
