from flask import Flask, render_template

class Hoja_Punteo:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'home', self.home)
        
    def home(self):
        return render_template('index.html')
        
    def run(self):
        self.app.run(host='0.0.0.0', port=8000, debug=True)

# Instanciamos la clase de manera global
app_instance = Hoja_Punteo()

# Exponemos la variable 'app' para que Gunicorn la encuentre en Render
app = app_instance.app 

if __name__ == '__main__':
    # Esto solo correrá si lo pruebas en tu compu local
    app_instance.run()