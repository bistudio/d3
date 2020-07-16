import sqlite3
import os.path
import json
import collections
from datetime import datetime as dt

db_file = '../app/site.db'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_file)

# select from sqlite database

con = sqlite3.connect(db_path)
cur = con.cursor()


selected_date = dt.utcnow()
selected_year = dt.utcnow().year
selected_month = dt.utcnow().month

select_covid_sql = """
SELECT  date_reported
,       day_number
,       month_number
,       year_number
,       cases
,       deaths
,       country_name
,       country_code
,       country_terr_code
,       populationData2019
,       continent
,       cum_num_14_days_cases_per_100K

FROM    covid19_historical_data 
WHERE   date_reported >= '2020-06-01 00:00:00'
and country_code In ('UK','US','BR','CZ','GH')
;
"""

# WHERE   date_reported >= (SELECT DATE('now', 'start of year', '-1 year') )

cur.execute(select_covid_sql)

rows = cur.fetchall()

rowarray_list = []
for row in rows:
    t = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
    rowarray_list.append(t)

j = json.dumps(rowarray_list)
rowarrays_file = 'data/covid.json'

with open(rowarrays_file, 'w') as f:
    f.writelines(j)

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['date_reported'] = row[0]
    d['day_number'] = row[1]
    d['month_number'] = row[2]
    d['year_number'] = row[3]
    d['cases'] = row[4]
    d['deaths'] = row[5]
    d['country_name'] = row[6]
    d['country_code'] = row[7]
    d['country_terr_code'] = row[8]
    d['populationData2019'] = row[9]
    d['continent'] = row[10]
    d['cum_num_14_day_cases_per_100k'] = row[11]
    objects_list.append(d)

j = json.dumps(objects_list)
objects_file = 'data/covid.json'
with open(objects_file, 'w') as f:
    f.writelines(j)

con.commit()
con.close()
