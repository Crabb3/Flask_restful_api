from flask_restful import Resource
from flask import request
from models.UserModel import UserModel, users
from models.UserSchema import UserSchema

user_schema = UserSchema() # many = True沒加會沒輸出
class User(Resource):

    def get(self, username):
        res = UserModel.getUser(username)
        return {
            "user" : user_schema.dump(res)
        }

    def post(self,username):
        json_data = request.json
        args = user_schema.load(json_data)
        newUser = UserModel(username,args['email'])
        UserModel.addUser(newUser)
        return {
            "message" : "add user success"
        } , 201

    def put(self,username):
        json_data = request.json
        args = user_schema.load(json_data)

        user = UserModel.getUser(username)

        user.email = args["email"]

        UserModel.updateUser()

        return {
            "message" : "update success"
        } , 201
    def delete(self,username):
        user = UserModel.getUser(username)
        UserModel.delUser(user)
        return {
            "message" : "delete success"
        } , 201

class Users(Resource):
    def get(self):
        res = UserModel.getAllUser()
        return {
            "user": user_schema.dump(res,many=True)
        },201