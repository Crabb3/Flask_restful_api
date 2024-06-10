from flask import Flask
from flask_restful import Api
from resources.user import User,Users
from common.utils import db,ma

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

api = Api(app)
api.add_resource(User,"/user/<username>")
api.add_resource(Users,"/user")


if "__main__" == __name__:
    db.init_app(app)
    ma.init_app(app)
    from models.UserModel import UserModel
    with app.app_context():
        db.create_all()
    app.run(debug = True)