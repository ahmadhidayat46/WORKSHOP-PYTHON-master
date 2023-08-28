from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Singkut2"

# Konfigurasi database
userpass = "mysql+pymysql://root:@"
basedir = "127.0.0.1"
dbname = "/responsi_python"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class DataMahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telp = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(250), nullable=False)

    def __init__(self, name, email, telp, address):
        self.name = name
        self.email = email
        self.telp = telp
        self.address = address

@app.route('/')
def index():
    data_mhs = DataMahasiswa.query.all()
    return render_template('index.html', data=data_mhs)

@app.route('/input', methods=['GET','POST'])
def input_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        telp = request.form['telp']
        address = request.form['address']

        add_data = DataMahasiswa(name,email,telp,address)

        db.session.add(add_data)
        db.session.commit()

        flash('Input Data Berhasil!')

        return redirect(url_for('index'))

    return render_template('input.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    data = DataMahasiswa.query.get_or_404(id)

    if request.method == 'POST':
        data.name = request.form['name']
        data.email = request.form['email']
        data.telp = request.form['telp']
        data.address = request.form['address']
        db.session.commit()

        flash('Edit Data Berhasil!')
        return redirect(url_for('index'))

    return render_template('edit.html', data=data)

@app.route('/delete/<int:id>')
def delete(id):
    data = DataMahasiswa.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()

    flash('Delete Berhasil!')
    return redirect(url_for('index'))
