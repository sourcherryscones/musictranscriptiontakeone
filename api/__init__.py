import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.svelte')

from flask import Flask
from config import Config
from api.extensions import db

'''
import boto3
login_manager = LoginManager()
from .sthree import s3_client
# removed db = SQLAlchemy() and the globals at the top of create_app; wondering if that does anything
'''

def create_app(conf_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(conf_class)

    #extensions!
    db.init_app(app)

    #blueprints!
    from api.main import bp as mainbp
    app.register_blueprint(mainbp)


    from api.auth import auth as authbp
    app.register_blueprint(authbp)

    return app