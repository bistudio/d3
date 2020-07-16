from app import app
from flask import render_template, redirect, request, url_for
from app.models import Country, Covid19HistoricalData
# import app.read_data as data_reader
from app.form import CountryForm
import json


@app.route('/')
@app.route('/home')
def home():
    form = CountryForm()
    with open('./app/data/covid.json', 'r') as f:
        covid_data = f.read()

    obj = json.loads(covid_data)

    return render_template('d3_dashboard.html', form=form, covid_data=obj, title="Covid-19 Dashboard")
