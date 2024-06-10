from common.utils import ma
from models.UserModel import UserModel

class UserSchema(ma.Schema):
    email = ma.Email(required=True)
    class Meta:
        model = UserModel
        fields = ('id','name','email') # jsonify後的資料要有哪些