"""
Punto de entrada principal del servidor Flask.
Registra los Blueprints (controladores) y arranca la aplicación.
"""

from flask import Flask
from flask_cors import CORS


from controllers.producto_controller import producto_blueprint

app = Flask(__name__)


CORS(app)


app.register_blueprint(producto_blueprint, url_prefix="/api")

@app.route("/")
def home():
    return "Backend Flask funcionando correctamente, y esta listo ser usado"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

