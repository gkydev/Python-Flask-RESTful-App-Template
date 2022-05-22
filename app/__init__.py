from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from flask_cors import CORS
from itsdangerous import URLSafeTimedSerializer
from flask_migrate import Migrate


app = Flask(__name__)
rest_api = Api(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
CORS(app)
usts = URLSafeTimedSerializer("secret-key")
migrate = Migrate()
migrate.init_app(app, db)

app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:passwor@localhost:5432/app"
app.config['JWT_SECRET_KEY'] = "jwt-secret-key"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
app.config['PROPAGATE_EXCEPTIONS'] = True

from app import routes