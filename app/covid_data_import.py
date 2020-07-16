import csv
import sqlite3
import os.path
from datetime import datetime as dt

db_file = '../app/site.db'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_file)

# insert into sqlite database

con = sqlite3.connect(db_path)
cur = con.cursor()

with open('covid-19.csv', 'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    next(dr)
    # Nested lists, tuples are used for executemany, not for execute.
    to_db = [(i['daterep'], i['day'], i['month']
              , i['year'], i['cases'], i['deaths'], i['country_name']
              , i['country_code'], i['countryterritorycode']
              , i['popData2019'], i['continent'], i['cum_num_14_days_of_cases_per_100K']) for i in dr]

create_table_sql = """CREATE TABLE IF NOT EXISTS covid19_historical_data (
id INTEGER not null	primary key,
date_reported DATETIME not null,
day_number SMALLINT not null,
month_number SMALLINT not null,
year_number SMALLINT not null,
cases INTEGER,
deaths INTEGER,
country_name VARCHAR(100) not null,
country_code VARCHAR(4),
country_terr_code VARCHAR(4),
populationData2019 INTEGER,
continent VARCHAR(40) not null,
cum_num_14_days_cases_per_100K FLOAT
);
"""
cur.execute(create_table_sql)
cur.execute("DELETE FROM main.covid19_historical_data;")
cur.executemany("INSERT INTO main.covid19_historical_data (date_reported, day_number, month_number, year_number"
                ", cases, deaths, country_name, country_code, country_terr_code"
                ",populationData2019,continent,cum_num_14_days_cases_per_100K"
                ") VALUES (?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?);", to_db)


con.commit()
con.close()
