import os
from flask import Flask, jsonify
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))


def importar_modelos_alchemy():
    import saludtech.modules.gestion_descargas.infraestructura.dto
    
def registrar_handlers():
    import saludtech.modules.gestion_descargas.aplicacion
    
def comenzar_consumidores(app):
    print('comenzar_consumidores')
    import saludtech.modules.procesamiento_imagenes.infraestructura.consumidores as procesamiento_imagenes
    
    import threading
    threading.Thread(target=procesamiento_imagenes.subscribirse_a_eventos, args=(app,)).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/saludtech'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'

     # Inicializa la DB
    from saludtech.config.db import init_db
    init_db(app)

    from saludtech.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()
    
    with app.app_context():
        db.create_all()
        comenzar_consumidores(app)

     # Importa Blueprints
    from . import gestion_descargas

    # Registro de Blueprints
    app.register_blueprint(gestion_descargas.bp)

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