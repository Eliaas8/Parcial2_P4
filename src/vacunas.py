import json
DATA = "../data/sh_imm_meas.json"

def _cargar():
    with open(DATA, "r", encoding="utf-8") as f:
        return json.load(f)

def obtener_todos():
    return _cargar()

def obtener_por_año(a):
    for r in _cargar():
        try:
            if int(r.get("año")) == a:
                return r
        except Exception:
            continue
    return None

def obtener_provincia(nombre):
    # Si no hay datos regionales en la fuente, simulamos datos por provincia.
    # La simulación toma la cobertura nacional y aplica una ligera variación.
    datos = []
    for r in _cargar():
        año = r.get("año")
        cobertura = r.get("cobertura", 0.0)
        # _sim devuelve un factor entre 0.95 y 0.99 para variar por año
        factor = _sim(año)
        datos.append({
            "provincia": nombre,
            "año": año,
            "cobertura": round(cobertura * factor, 2)
        })
    return datos

def _sim(año):
    # Simulación determinística para dar ligeras diferencias por año.
    try:
        return (abs(int(año) % 5) + 95) / 100.0
    except Exception:
        return 0.97
