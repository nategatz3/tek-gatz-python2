import os
from forms import  AddPuppyForm , DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
# Old SQLite Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
# New MySQL Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password123@localhost/puppies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'pups'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        if self.owner:
            return f"Puppy {self.name} is {self.age} months old and lives with {self.owner.name}"
        else:
            return f"Puppy {self.name} is {self.age} months old and lives in the wilderness"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('pups.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"

db.create_all()
############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_puppy', methods=['GET', 'POST'])
def add_pup():
    form = AddPuppyForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

        # Adds Pup to db
        new_pup = Puppy(name,age)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_puppy.html',form=form)

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data

        # Adds Owner to db
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html',form=form)

@app.route('/list')
def list_pup():
    # Shows all the Pups in the db
    pups = Puppy.query.all()
    return render_template('list_puppy.html', pups=pups)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
