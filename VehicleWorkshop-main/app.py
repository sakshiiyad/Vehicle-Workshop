from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///workshop_db.db"
db = SQLAlchemy(app)

class Hundai(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200),nullable=True)
    vehicle_no = db.Column(db.String(200), nullable=False)
    work_desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self)->str:
        return f"{self.sno} - {self.vehicle_no} - {self.work_desc} - {self.date_created}"

class Tata(db.Model):
    name=db.Column(db.String(200),nullable=False)
    sno = db.Column(db.Integer, primary_key=True)
    vehicle_no = db.Column(db.String(200), nullable=False)
    work_desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
class MarutiSuzuki(db.Model):
    name=db.Column(db.String(200),nullable=False)
    sno = db.Column(db.Integer, primary_key=True)
    vehicle_no = db.Column(db.String(200), nullable=False)
    work_desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    
class Ford(db.Model):
    name=db.Column(db.String(200),nullable=False)
    sno = db.Column(db.Integer, primary_key=True)
    vehicle_no = db.Column(db.String(200), nullable=False)
    work_desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Fiat(db.Model):
    name=db.Column(db.String(200),nullable=False)
    sno = db.Column(db.Integer, primary_key=True)
    vehicle_no = db.Column(db.String(200), nullable=False)
    work_desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/Hundai',methods=['GET','POST'])
def Hundai_func():
    if request.method=='POST':
        name=request.form['name']
        vehicle_no=request.form['vehicle_no']
        work_desc=request.form['work_desc']
        hundai=Hundai(vehicle_no=vehicle_no,work_desc=work_desc,name=name)
        db.session.add(hundai)
        db.session.commit()
    vehicle=Hundai.query.all()
    return render_template('Hundai.html',vehicle=vehicle)

@app.route('/Tata',methods=['GET','POST'])
def Tata_func():
    if request.method=='POST':
        name=request.form['name']
        vehicle_no=request.form['vehicle_no']
        work_desc=request.form['work_desc']
        tata=Tata(vehicle_no=vehicle_no,work_desc=work_desc,name=name)
        db.session.add(tata)
        db.session.commit()
    vehicle=Tata.query.all()
    return render_template('Tata.html',vehicle=vehicle)

@app.route('/MarutiSuzuki',methods=['GET','POST'])
def MarutiSuzuki_func():
    if request.method=='POST':
        name=request.form['name']
        vehicle_no=request.form['vehicle_no']
        work_desc=request.form['work_desc']
        maruti=MarutiSuzuki(vehicle_no=vehicle_no,work_desc=work_desc,name=name)
        db.session.add(maruti)
        db.session.commit()
    vehicle=MarutiSuzuki.query.all()
    return render_template('MarutiSuzuki.html',vehicle=vehicle)

@app.route('/Fiat',methods=['GET','POST'])
def Fiat_func():
    if request.method=='POST':
        name=request.form['name']
        vehicle_no=request.form['vehicle_no']
        work_desc=request.form['work_desc']
        fiat=Fiat(vehicle_no=vehicle_no,work_desc=work_desc,name=name)
        db.session.add(fiat)
        db.session.commit()
    vehicle=Fiat.query.all()
    return render_template('Fiat.html',vehicle=vehicle)

@app.route('/Ford',methods=['GET','POST'])
def Ford_func():
    if request.method=='POST':
        name=request.form['name']
        vehicle_no=request.form['vehicle_no']
        work_desc=request.form['work_desc']
        ford=Ford(vehicle_no=vehicle_no,work_desc=work_desc,name=name)
        db.session.add(ford)
        db.session.commit()
    vehicle=Ford.query.all()
    return render_template('Ford.html',vehicle=vehicle)

@app.route('/delete/<int:sno>')
def delete_hundai(sno):
    hundai=Hundai.query.filter_by(sno=sno).first()
    db.session.delete(hundai)
    db.session.commit()
    return redirect("/Hundai")

@app.route('/delete_tata/<int:sno>')
def delete_tata(sno):
    tata=Tata.query.filter_by(sno=sno).first()
    db.session.delete(tata)
    db.session.commit()
    return redirect("/Tata")

@app.route('/delete_maruti/<int:sno>')
def delete_marutiSuzuki(sno):
    maruti=MarutiSuzuki.query.filter_by(sno=sno).first()
    db.session.delete(maruti)
    db.session.commit()
    return redirect("/MarutiSuzuki")

@app.route('/delete_fiat/<int:sno>')
def delete_fiat(sno):
    fiat=Fiat.query.filter_by(sno=sno).first()
    db.session.delete(fiat)
    db.session.commit()
    return redirect("/Fiat")

@app.route('/delete_ford/<int:sno>')
def delete_Ford(sno):
    ford=Ford.query.filter_by(sno=sno).first()
    db.session.delete(ford)
    db.session.commit()
    return redirect("/Ford")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=8000, debug=True)
