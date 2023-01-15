import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from decouple import config 

firebase_sdk = credentials.Certificate(config('FIREBASE_CERTIFICATE'))
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':config('DATABASE_URL')})


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