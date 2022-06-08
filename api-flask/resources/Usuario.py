from flask_restful import Resource, reqparse
from models.usuario_modelo import UserModel


class Users(Resource):
    def get(self):
        # SELECT * FROM usuarios
        return {'usuarios': [user.json() for user in UserModel.query.all()]}


class User(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('login', type=str, required=True, help="The field 'login' must be informed")
    argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' must be informed")

    # /usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404  # not found

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
                return {'message': 'User deleted.'}
            except:
                return {'message': 'An internal error has occurred trying to delete user.'}, 500
        return {'message': 'User not found.'}, 404

class UserRegister(Resource):
  # /cadastro
  def post(self):
    atributos = reqparse.RequestParser()
    atributos.add_argument('login', type=str, required=True, help="The field 'login' must be informed")
    atributos.add_argument('senha', type=str, required=True, help="The field 'senha' must be informed")
    dados = atributos.parse_args()

    if UserModel.find_by_login(dados['login']):
      return {"message": "The login '{}' already exists.".format(dados['login'])}
    
    user = UserModel(**dados)
    user.save_user()
    return {"message": "User created!"}, 201 # created