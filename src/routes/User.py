from flask import Blueprint,jsonify,request
from models.UserModel import UserModel

main = Blueprint('user_blueprint',__name__)

@main.route('/user',methods=['POST'])
def get_user():
    try:
        em = request.json['email']
        u = UserModel.get_user_email(email=em)
        print(u)
        return jsonify(u),200 

    except Exception as e:
        return jsonify({'messagee':str(e)}),404

@main.route('/add',methods=['POST'])
def add_user():
    try:

        email = request.json['email']
        name = request.json['name']
        password = request.json['password']
        birth = request.json['birth']
        
        us = {  
            'email':email,
            'name': name,
            'password':password,
            'birth':birth
        }
        print("new_user",us)

        UserModel.add_user(us)

        return us

    except Exception as ex:
        return jsonify({'messagee':str(ex)}),404

@main.route('/auth',methods=['POST'])
def authUser():

    try:
        
        email = request.json['email']
        password = request.json['password']
        condition = UserModel.verifyUser(email=email,password=password)

        if(condition == "Not found" or condition == "Cretendials incorrects"):
            return jsonify({'message':condition}),404
        else:
            return jsonify(condition),200 


    except Exception as ex:
        return jsonify({'messagee':str(ex)}),404


