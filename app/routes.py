from app import app
from flask import render_template, redirect, request, url_for
from app.models import Country, Covid19HistoricalData
# import app.read_data as data_reader
from app.form import CountryForm
from app.models import Country
import json


@app.route('/')
@app.route('/home')
def home():
    form = CountryForm()

    sc = Country.query.filter_by(id=form.country_name.data.id).first()
    sc_code = form.country_name.data.country_code

    with open('./app/data/covid.json', 'r') as f:
        covid_data = f.read()

    obj = json.loads(covid_data)

    return render_template('d3_dashboard.html', form=form, covid_data=obj, sc_code=sc_code, title="Covid-19 Dashboard")


@app.route('/d3_enter')
def d3_enter():
    return render_template('general_update_pattern.html')


@app.route('/d3_exit')
def d3_exit():
    return render_template('d3_exit.html')


@app.route('/d3_update')
def d3_update():
    return render_template('d3_update.html')
