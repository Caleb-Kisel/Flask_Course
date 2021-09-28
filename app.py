import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from security import autheticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://ibrxjdlampinsi:a36c0b94d529e0d3c90413a4c94992130b187688cdf18f67ce8216f9e0bcefa2@ec2-44-195-201-3.compute-1.amazonaws.com:5432/daeq16v9iqoll', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'arturo'
api = Api(app)

jwt = JWT(app, autheticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)