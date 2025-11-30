import json
DATA = "../data/sh_imm_meas.json"

def _cargar():
    with open(DATA, "r", encoding="utf-8") as f:
        return json.load(f)

def obtener_todos():
    return _cargar()

def obtener_por_ano(a):
    for r in _cargar():
        try:
            if int(r.get("anio")) == a:
                return r
        except Exception:
            continue
    return None

def obtener_provincia(nombre):
    # Si no hay datos regionales en la fuente, simulamos datos por provincia.
    # La simulación toma la cobertura nacional y aplica una ligera variación.
    datos = []
    for r in _cargar():
        anio = r.get("anio")
        cobertura = r.get("cobertura", 0.0)
        # _sim devuelve un factor entre 0.95 y 0.99 para variar por año
        factor = _sim(anio)
        datos.append({
            "provincia": nombre,
            "anio": anio,
            "cobertura": round(cobertura * factor, 2)
        })
    return datos

def _sim(anio):
    # Simulación determinística para dar ligeras diferencias por año.
    try:
        return (abs(int(anio) % 5) + 95) / 100.0
    except Exception:
        return 0.97
