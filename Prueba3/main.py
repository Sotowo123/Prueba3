from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Ejercicio1', methods=['GET', 'POST'])

def Ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1+nota2+nota3)/3
        if promedio >=4:
            resultado = "aprobado"
        if promedio < 4 or asistencia < 75:
            resultado = "reprobado"

        return render_template('Ejercicio1.html', resultado=resultado, nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia)
    return render_template('Ejercicio1.html', resultado=None, nota1=0, nota2=0, nota3=0, asistencia=0)

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def Ejercicio2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        largo = 0
        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            mayor = nombre1
            largo = len(nombre1)
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            mayor = nombre2
            largo = len(nombre2)
        elif len(nombre3) > len(nombre1) and len(nombre3) > len(nombre2):
            mayor = nombre3
            largo = len(nombre3)
        else:
            mayor = "Hay empate"
            largo = None
        return render_template('Ejercicio2.html', nombre1=nombre1, nombre2=nombre2, nombre3=nombre3, mayor=mayor,
                               largo=largo)
    return render_template('Ejercicio2.html', nombre1=None, nombre2=None, nombre3=None, mayor=None, largo=None)
if __name__ == '__main__':
    app.run(debug=True)
