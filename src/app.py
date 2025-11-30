from flask import Flask, jsonify
from vacunas import obtener_todos, obtener_por_ano, obtener_provincia

app = Flask(__name__)

@app.get("/vacunas")
def todas_vacunas():
    return jsonify(obtener_todos())

@app.get("/vacunas/<int:ano>")
def vacuna_por_ano(ano):
    r = obtener_por_ano(ano)
    return (jsonify(r), 200) if r else (jsonify({"error": "No encontrado"}), 404)

@app.get("/vacunas/provincia/<nombre>")
def vacunas_por_provincia(nombre):
    return jsonify(obtener_provincia(nombre))

if __name__ == "__main__":
    app.run()
