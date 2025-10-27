from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy                         #flask_SQLAlchemy is the extension of SQLAlchemy to work with SQL databases 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'   # app_name.congif[] : to add configuration settings to the app . SQLALCHEMY_DATABASE_URI is the configuration key
db = SQLAlchemy(app)

class Item(db.Model):     # Item is model stored in db
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
