import os
from flask import render_template, flash
from scheduler import app
from scheduler.forms import RunModel

@app.route('/') #Page to display tiles
def home():

    return render_template('home.html')

@app.route('/train') #Page to display tiles
def train_model():

    #form = SetKbase()

    return render_template('train_model.html')

@app.route('/run') #Page to display tiles
def run_model():

    form = RunModel()

    return render_template('run_model.html',title='RunModel', form=form)

@app.route('/data') #Page to display tiles
def data():

    #form = SetKbase()

    return render_template('data.html')