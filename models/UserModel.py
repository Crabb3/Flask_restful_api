from common.utils import db

users = []
class UserModel(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique=True, nullable = False)
    email = db.Column(db.String(120), nullable = False)

    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    @classmethod
    def getUser(cls,name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def getAllUser(cls):
        return cls.query.all()

    def addUser(self):
        db.session.add(self)
        db.session.commit()
    
    def delUser(self):
        db.session.delete(self)
        db.session.commit()
    
    def updateUser():
        db.session.commit()