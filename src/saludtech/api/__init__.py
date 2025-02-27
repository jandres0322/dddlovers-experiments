import os
from flask import Flask, jsonify
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:(7KH,{k4CdK>DQ1]@35.194.32.155/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'

     # Inicializa la DB
    from saludtech.config.db import init_db
    init_db(app)

    from saludtech.config.db import db
    from saludtech.modulos.imagenes.infraestructura.dto import EntregaImagenORM, HistorialEntregaORM
    with app.app_context():
        db.create_all()

     # Importa Blueprints
    from . import imagenes

    # Registro de Blueprints
    app.register_blueprint(imagenes.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app