import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db
from datetime import datetime
from decouple import config 
from models.entities import User
from utils.Utils import Utils


firebase_sdk = credentials.Certificate(config('FIREBASE_JSON'))
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':config('DATABASE_URL')})

class UserModel():

    @classmethod
    def get_user_email(self,email):

        #res = auth.get_user_by_email(email)
        #print(res)
        #u = User(id=str(res.uid),name=str(res.display_name),email=str(res.email))
        ref = db.reference()
        users = ref.child('users').get()
        for user in users.values() :
            #print(user)
            if(user['email']==email):
                return user 

        return {'message':"Not Found"}

    @classmethod
    def add_user(self,us):
        ref = db.reference('users')
        new_user = {
            'username': us['name'],
            'email': us['email'],
            'password': Utils.txt2Sha3(us['password']),
            'birth': Utils.getAge(us['birth']),
            'joined': str(datetime.now().strftime('%d/%m/%Y'))
        }

        ref.push().set( new_user)

    @classmethod
    def verifyUser(self,email,password):

        user = UserModel.get_user_email(email)
        if('message' in user):
            return "Not found"
        else:
            if(user['password'] == Utils.txt2Sha3(password)):
                return user
            else:
                return "Cretendials incorrects"

    