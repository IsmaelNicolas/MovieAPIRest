import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import hashlib

# Calculamos el resumen SHA-3 de una cadena de texto
text = 'hello world'
text_sha3 = hashlib.sha3_256(text.encode('utf-8')).hexdigest()
print(text_sha3)  # Output: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08


firebase_sdk = credentials.Certificate("src\cinect-372019-firebase-adminsdk-omx2o-68831cf737.json")
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://cinect-372019-default-rtdb.firebaseio.com/'})

root_ref = db.reference()

# Creamos un nuevo nodo en la base de datos
def create_node(path, data):
  try:
    ref = root_ref.child(path)
    ref.set(data)
    print(f'Successfully created node at {path}')
  except Exception as e:
    print(e)

# Leemos un nodo existente
def read_node(path):
  try:
    ref = root_ref.child(path)
    data = ref.get()
    print(f'Successfully retrieved data from {path}: {data}')
  except Exception as e:
    print(e)

# Actualizamos un nodo existente
def update_node(path, data):
  try:
    ref = root_ref.child(path)
    ref.update(data)
    print(f'Successfully updated node at {path}')
  except Exception as e:
    print(e)

# Borramos un nodo existente
def delete_node(path):
  try:
    ref = root_ref.child(path)
    ref.delete()
    print(f'Successfully deleted node at {path}')
  except Exception as e:
    print(e)

# Creamos un nuevo nodo en la base de datos
create_node('reviews', {'userId': 'NNsJZAucqlBvLlig3Vm', 'movieId': '411','user_score':'4','user_comment':'It is amazing','date_score':'2023/2/9'})


# Borramos el nodo
#delete_node('users/1')