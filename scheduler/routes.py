import os
from flask import render_template, flash
from scheduler import app
from scheduler.forms import RunModel

@app.route('/') #Home page
def home():

    return render_template('home.html')

@app.route('/train') #Page to allow you to train model
def train_model():

    #form = SetKbase()

    return render_template('train_model.html')

@app.route('/run', methods=['GET', 'POST']) #Page to allow you to run model
def run_model():

    form = RunModel()

    return render_template('run_model.html',title='RunModel', form=form)

@app.route('/data') #Page to manage data
def data():

    #form = SetKbase()

    return render_template('data.html')