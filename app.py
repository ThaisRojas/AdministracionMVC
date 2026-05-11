from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super_secreto_para_flash_messages"


ISLAS = [
    {"id": 1, "nombre": "Santa Cruz"},
    {"id": 2, "nombre": "San Cristóbal"},
    {"id": 3, "nombre": "Isabela"}
]

@app.route('/')
def inicio():
    return redirect(url_for('crear_viaje'))

@app.route('/api/destinos/<int:origen_id>')
def obtener_destinos(origen_id):
    destinos_validos = [isla for isla in ISLAS if isla['id'] != origen_id]
    return jsonify(destinos_validos)


@app.route('/admin/viajes/crear', methods=['GET', 'POST'])
def crear_viaje():
    if request.method == 'POST':
        origen_id = request.form.get('origen_id')
        destino_id = request.form.get('destino_id')
        fecha_str = request.form.get('fecha_salida')
        
        # 1. Validar que vengan los datos
        if not origen_id or not destino_id or not fecha_str:
            flash("Todos los campos son obligatorios", "danger")
            return redirect(url_for('crear_viaje'))

        # 2. VALIDACIÓN ESTRICTA BACKEND 
        fecha_salida = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        fecha_actual = datetime.now().date()

        if fecha_salida < fecha_actual:
            flash("ERROR DE SEGURIDAD: No se pueden programar viajes con fechas en el pasado.",)
            return redirect(url_for('crear_viaje'))
        
        flash(" Viaje creado y guardado exitosamente en la base de datos.", )
        return redirect(url_for('crear_viaje'))

    return render_template('admin_crear_viaje.html', islas=ISLAS)

if __name__ == '__main__':
    app.run(debug=True)
    