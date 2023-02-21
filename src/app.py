from flask import Flask
from config import config
from flask_cors import CORS
import ssl
# Routes
from routes import Movie
from routes import User
from routes import Email

app = Flask(__name__)

CORS(app)

def page_not_found(error):
    return "<h1>Not Fount</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Movie.main, url_prefix='/api/movies')
    app.register_blueprint(User.main, url_prefix='/api/users')
    app.register_blueprint(Email.main, url_prefix='/api/email')

    # error handler
    app.register_error_handler(404, page_not_found)

    # run app
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain("cert.pem","key.pem")
    app.run(host='0.0.0.0',port=8000,debug=True,ssl_context=context)
