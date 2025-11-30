# API Sarampión Panamá 

Estructura:
- src/: código fuente (app.py, vacunas.py)
- data/: JSON con datos (sh_imm_meas.json)
- tests/: pruebas unitarias (pytest)

Ejecutar local:
1. Ir a la carpeta src
2. python app.py

Endpoints:
- GET /vacunas
- GET /vacunas/<año>
- GET /vacunas/provincia/<nombre>

Test:
Desde la raíz del proyecto:
pip install pytest flask
cd src
pytest ../tests
