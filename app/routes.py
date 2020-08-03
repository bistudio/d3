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

    default_selected_country = form.country_name.data.country_code

    with open('./app/data/covid.json', 'r') as f:
        covid_data = f.read()

    obj = json.loads(covid_data)

    return render_template('d3_dashboard.html', form=form, covid_data=obj
                           , default_selected_country=default_selected_country, title="Covid-19 Dashboard")


@app.route('/d3_general_update_pattern')
def d3_general_update_pattern():
    return render_template('general_update_pattern.html')


@app.route('/d3_scale')
def d3_scale():
    return render_template('d3_scale.html')


@app.route('/d3_update')
def d3_update():
    return render_template('d3_update.html')


@app.route('/d3_path')
def d3_path():
    return render_template('d3_path.html')


@app.route('/d3_animate')
def d3_animate():
    return render_template('d3_animate.html')


@app.route('/d3_arc')
def d3_arc():
    return render_template('d3_arc.html')

@app.route('/d3_bar_chart')
def d3_bar_chart():
    return render_template('d3_bar_chart.html')
