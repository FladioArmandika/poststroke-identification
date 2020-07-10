from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('beranda.html')

@app.route('/bantuan')
def pengujian():
    return render_template('bantuan.html')

@app.route('/menu')
def bantuan():
    return render_template('menu.html')

@app.route('/optimalisasi')
def optimalisasi():
    return render_template('optimalisasi.html')

@app.route('/identifikasi')
def identifikasi():
    return render_template('identifikasi.html')

@app.route('/datalatih')
def datalatih():
    return render_template('datalatih.html')


# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 3000))
#     app.run()
